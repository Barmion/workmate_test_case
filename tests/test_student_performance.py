from performance_analyzer.reports import StudentPerfomanceReport


def test_empty_data():
    report = StudentPerfomanceReport([])
    result = report.get_report()
    assert result == []


def test_single_student_single_grade(sample_records):
    record = sample_records(num_students=1, records_per_student=1)
    report = StudentPerfomanceReport(record)
    result = report.get_report()

    assert len(result) == 1
    assert result[0][1] == record[0].grade


def test_get_average_grade(single_student_average_grade):
    records, average_grade = single_student_average_grade
    report = StudentPerfomanceReport(records)
    result = report.get_report()

    assert result[0][1] == average_grade


def test_multiple_students(sample_records):
    num_students = 5
    records = sample_records(num_students=num_students, records_per_student=1)
    report = StudentPerfomanceReport(records)
    result = report.get_report()

    assert len(result) == num_students


def test_sorting_order(sample_records):
    records = sample_records(num_students=5, records_per_student=5)
    report = StudentPerfomanceReport(records)
    result = report.get_report()
    sorted_result = sorted(result, key=lambda x: x[1], reverse=True)

    assert result == sorted_result


def test_print_empty_report(mock_printer):
    report = StudentPerfomanceReport([])
    report.print_report()
    output = '\n'.join(mock_printer)

    assert 'student_name' in output
    assert 'average_grade' in output


def test_print_report_format(sample_records, mock_printer):
    records = sample_records(num_students=2, records_per_student=2)
    report = StudentPerfomanceReport(records)
    report.print_report()
    output = '\n'.join(mock_printer)

    assert 'student_name' in output
    assert 'average_grade' in output
    for record in records:
        assert record.student_name in output
