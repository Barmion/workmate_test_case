from unittest.mock import patch

import pytest

from performance_analyzer.main import parse_script_args


@patch(
    'sys.argv',
    [
        '-m performanse_analizer.main',
        '-f', 'data/students1.csv',
        '-r', 'student-performance',
    ]
)
def test_parse_short_args():
    """Парсер считывает аргументы по коротким названиям."""
    args = parse_script_args()
    assert args.files == ['data/students1.csv']
    assert args.report == 'student-performance'


@patch(
    'sys.argv',
    [
        '-m performanse_analizer.main',
        '--files', 'data/students1.csv',
        '--report', 'student-performance',
    ]
)
def test_parse_full_args():
    """Парсер считывает аргументы по полным названиям."""
    args = parse_script_args()
    assert args.files == ['data/students1.csv']
    assert args.report == 'student-performance'


@patch(
    'sys.argv',
    [
        '-m performanse_analizer.main',
        '-r', 'student-performance',
    ]
)
def test_parse_no_files_args():
    """Ошибка, если не указать аргумент --files."""
    with pytest.raises(SystemExit):
        _ = parse_script_args()


@patch(
    'sys.argv',
    [
        '-m performanse_analizer.main',
        '-f', 'data/students1.csv',
    ]
)
def test_parse_no_report_args():
    """Ошибка, если не указать аргумент --report."""
    with pytest.raises(SystemExit):
        _ = parse_script_args()


@patch(
    'sys.argv',
    [
        '-m performanse_analizer.main',
        '-f', 'data/students1.csv',
        '-r', 'student-performance', 'student-performance',
    ]
)
def test_parse_multiple_report_args():
    """Ошибка, если передать в аргумент --report несколько параметров."""
    with pytest.raises(SystemExit):
        _ = parse_script_args()


@patch(
    'sys.argv',
    [
        '-m performanse_analizer.main',
        '-f', 'performanse_analizer/data/students1.csv',
              'performanse_analizer/data/students2.csv',
        '-r', 'student-performance',
    ]
)
def test_parse_multiple_files_args():
    """Аргумент --files может принимать несколько параметров."""
    args = parse_script_args()
    assert len(args.files) == 2
