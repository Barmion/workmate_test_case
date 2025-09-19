from pathlib import Path
from datetime import datetime

import pytest
from faker import Faker

from performance_analyzer.utils import PerfomanceRecord


CURRENT_DIR = Path(__file__).resolve().parent


@pytest.fixture
def single_csv_path():
    file_path = CURRENT_DIR / 'data' / 'students1_t.csv'
    return [file_path,]


@pytest.fixture
def multiple_csv_path():
    file_path_1 = CURRENT_DIR / 'data' / 'students1_t.csv'
    file_path_2 = CURRENT_DIR / 'data' / 'students2_t.csv'
    return [file_path_1, file_path_2]


@pytest.fixture
def single_file_records():
    return [
        PerfomanceRecord(
            student_name='Иванов Алексей',
            subject='Математика',
            teacher_name='Петрова Ольга',
            date=datetime.strptime('2023-09-10', '%Y-%m-%d'),
            grade=5,
        )
    ]


@pytest.fixture
def multiple_file_records(single_file_records):
    return single_file_records + [
        PerfomanceRecord(
            student_name='Морозова Екатерина',
            subject='Физика',
            teacher_name='Сидоров Иван',
            date=datetime.strptime('2023-09-20', '%Y-%m-%d'),
            grade=5,
        )
    ]


@pytest.fixture
def fake():
    return Faker('ru_RU')


@pytest.fixture
def sample_records(fake):
    def _create_records(num_students=3, records_per_student=5):
        records = []
        subjects = ['Математика', 'Физика', 'Химия', 'История', 'Литература']

        for _ in range(num_students):
            student_name = fake.name()
            for _ in range(records_per_student):
                record = PerfomanceRecord(
                    student_name=student_name,
                    subject=fake.random.choice(subjects),
                    teacher_name=fake.name(),
                    date=datetime.now(),
                    grade=fake.random.randint(2, 5)
                )
                records.append(record)
        return records
    return _create_records


@pytest.fixture
def single_student_average_grade(fake):
    records = []
    grades = [fake.random.randint(2, 5) for _ in range(5)]
    average_grade = sum(grades) / len(grades)
    student_name = fake.name()
    for grade in grades:
        record = PerfomanceRecord(
            student_name=student_name,
            subject='Математика',
            teacher_name=fake.name(),
            date=datetime.now(),
            grade=grade
        )
        records.append(record)
    return records, average_grade


@pytest.fixture
def mock_printer(monkeypatch):
    printed_lines = []

    def mock_print(*args, **kwargs):
        printed_lines.append(' '.join(str(arg) for arg in args))

    monkeypatch.setattr('builtins.print', mock_print)
    return printed_lines
