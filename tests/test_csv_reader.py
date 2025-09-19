from performance_analyzer.utils import read_csv_files


def test_read_single_file(single_csv_path, single_file_records):
    """Конвертер корректно обрабатывает один файл."""
    data = read_csv_files(single_csv_path)
    assert data == single_file_records


def test_read_multiple_file(multiple_csv_path, multiple_file_records):
    """Конвертер корректно обрабатывает несколько файлов."""
    data = read_csv_files(multiple_csv_path)
    assert data == multiple_file_records
