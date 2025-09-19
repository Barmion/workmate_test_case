import pytest

from performance_analyzer.reports import (
    StudentPerfomanceReport,
    get_report_class,
)


def test_get_correct_report_class():
    """По корректным данным выдается корректный класс отчета."""
    report_class = get_report_class('student-performance')
    assert report_class == StudentPerfomanceReport


def test_parse_wrong_report_args():
    """Ошибка, если указать неверный класс отчета."""
    with pytest.raises(ValueError):
        _ = get_report_class('wrong-report')
