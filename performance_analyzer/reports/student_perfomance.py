from collections import defaultdict

from tabulate import tabulate

from .base_report import BaseReport


class StudentPerfomanceReport(BaseReport):

    def get_report(self) -> list[str, float]:
        students = defaultdict(lambda: {'total': 0, 'count': 0})
        for record in self.data:
            students[record.student_name]['total'] += record.grade
            students[record.student_name]['count'] += 1

        report = [
            (name, grades['total'] / grades['count'])
            for name, grades in students.items()
        ]
        report.sort(key=lambda x: x[1], reverse=True)
        return report

    def print_report(self):
        report = self.get_report()
        print(
            tabulate(
                report,
                headers=('student_name', 'average_grade'),
                tablefmt='grid',
                floatfmt='.2f',
                showindex=range(1, len(report) + 1),
            )
        )
