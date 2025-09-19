from .student_perfomance import StudentPerfomanceReport


_REPORTS = {
    'student-performance': StudentPerfomanceReport,
}


def get_report_class(report_name: str) -> type:
    if report_name not in _REPORTS:
        raise ValueError(
            f'Неизвестный отчет: {report_name}. '
            f'Список доступных отчетов: {_REPORTS.keys()}'
        )
    return _REPORTS[report_name]
