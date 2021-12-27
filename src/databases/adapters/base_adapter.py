from io import BytesIO
from typing import Dict, Any, Optional, List


class BaseAdapter:
    def add_elem_to_table(self, table_name: str, columns: Dict[str, Any],
                          file_columns: Optional[Dict[str, BytesIO]] = None):
        pass

    def filter_by_column_value(self, table_name: str,
                               columns_with_value: Optional[Dict[str, Any]]) -> List[Dict[str, Any]]:
        pass

    def get_table_size(self, table_name: str) -> int:
        pass
