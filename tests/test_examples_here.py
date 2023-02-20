from typing import Iterator

import os
from pathlib import Path

import pytest
from mypy import api
from PySide6.QtWidgets import QApplication

TESTS_DIR = Path(__file__).parent


def gen_file_list() -> Iterator[Path]:
    """List of all files included in the directory tests for typing checking them"""
    for path in TESTS_DIR.glob("*.py"):
        if not path.name.startswith("test_") and not path.name.startswith('X'):
            yield path



@pytest.fixture(name="qapplication", scope="session")
def qapplication_fixture() -> QApplication:
    application = QApplication.instance()
    if application is None:
        application = QApplication(['-platform', 'minimal'])

    return application

@pytest.mark.parametrize(
    "filepath",
    list(gen_file_list()),
    ids=[v.relative_to(TESTS_DIR).as_posix() for v in gen_file_list()],
)
def test_examples_with_mypy(filepath: Path) -> None:
    """Run mypy over example files."""
    stdout, stderr, exitcode = api.run([os.fspath(filepath)] + ['--show-error-codes'])
    if stdout:
        print(stdout)
    if stderr:
        print(stderr)

    assert stdout.startswith("Success: no issues found")
    assert not stderr
    assert exitcode == 0


@pytest.mark.parametrize(
    "filepath", list(gen_file_list()), ids=[v.name for v in gen_file_list()]
)
def test_examples_execution(filepath: Path, qapplication: QApplication) -> None:
    """Run the test files to make sure they work properly."""
    code = filepath.read_text(encoding="utf-8")
    exec(compile(code, filepath, "exec"), {})
