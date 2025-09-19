import csv
from dataclasses import dataclass
from datetime import datetime


@dataclass
class PerfomanceRecord:
    student_name: str
    subject: str
    teacher_name: str
    date: datetime
    grade: int


def read_csv_files(file_paths: list[str]) -> list[PerfomanceRecord]:
    data = []
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                record = PerfomanceRecord(
                    student_name=row['student_name'],
                    subject=row['subject'],
                    teacher_name=row['teacher_name'],
                    date=datetime.strptime(row['date'], '%Y-%m-%d'),
                    grade=int(row['grade'])
                )
                data.append(record)
    return data
