from io import BytesIO
from typing import Optional, Dict, Any, List

from src.databases.adapters.base_adapter import BaseAdapter
import psycopg2
import psycopg2.extras


class PostgresqlAdapter(BaseAdapter):
    def __init__(self, hostname, port, username, password, database):
        BaseAdapter.__init__(self)
        self.conn = psycopg2.connect(host=hostname, port=port, user=username, password=password, dbname=database)
        self.cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    def add_elem_to_table(self, table_name: str, columns: Dict[str, Any],
                          file_columns: Optional[Dict[str, BytesIO]] = None):
        keys = [key for key in columns] + \
               ([key for key in file_columns] if file_columns is not None else [])
        values = [columns[key] for key in columns] + \
                 ([file_columns[key].read() for key in file_columns] if file_columns is not None else [])
        self.cursor.execute(
            f"""
            INSERT INTO {table_name} ({",".join(keys)}) VALUES ({", ".join(["%s"] * len(keys))})
            """,
            values
        )
        self.conn.commit()

    def filter_by_column_value(self, table_name: str,
                               columns_with_value: Optional[Dict[str, Any]]) -> List[Dict[str, Any]]:
        self.cursor.execute(f"SELECT * FROM {table_name} " +
                            f"""
                            WHERE {" AND ".join([f'{key} = {columns_with_value[key]}' for key in columns_with_value])}
                            """
                            if columns_with_value is not None else ""
                            )
        return self.cursor.fetchall()

    def get_table_size(self, table_name: str) -> int:
        self.cursor.execute(f"SELECT count(*) FROM {table_name}")
        return int(list(dict(self.cursor.fetchone()).values())[0])

    def __del__(self):
        self.cursor.close()
        self.conn.close()
