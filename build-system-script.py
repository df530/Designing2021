import sys
import subprocess
from typing import List


def call_all(calls: List[str]):
    for call in calls:
        if subprocess.call(call.split()) != 0:
            raise RuntimeError(f"Call '{call}' failed")


def install_dependencies():
    calls = [
        "python3 -m pip install --upgrade pip",
        "python3 -m pip install -r requirements.txt"
    ]
    call_all(calls)


@NotImplementedError
def run_tests():
    pass
    # calls = [
    #     "python3 -m unittest tests/unit_tests.py",
    #     "python3 -m unittest tests/integration_tests.py"
    # ]
    # call_all(calls)


@NotImplementedError
def check_coverage():
    pass
    # calls = [
    #     "python3 -m coverage run -m unittest tests/unit_tests.py",
    #     "python3 -m coverage report -m"
    # ]
    # call_all(calls)


def run_flake8():
    calls = [
        "python3 -m flake8 src --count --select=E9,F63,F7,F82 --show-source --statistics",
        "python3 -m flake8 src --count --max-complexity=10 --max-line-length=120 --statistics",
    ]
    call_all(calls)


def run_pylint():
    calls = [
        "python3 -m pylint src"
    ]
    call_all(calls)


def run_type_checking():
    calls = [
        "python3 -m mypy src"
    ]
    call_all(calls)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise RuntimeError(f"Wrong number of arguments. Expected 2, found {len(sys.argv)}:\n"
                           f"{sys.argv}")
    command = sys.argv[1]
    if command == "install-depends":
        install_dependencies()
    elif command == "type-check":
        run_type_checking()
    # TODO
    # elif command == "test":
    #     run_tests()
    # elif command == "check-coverage":
    #     check_coverage()
    elif command == "flake8":
        run_flake8()
    elif command == "pylint":
        run_pylint()
    elif command == "all-checks":
        run_type_checking()
        run_flake8()
        run_pylint()
    else:
        raise RuntimeError(f"Wrong command '{command}'")
