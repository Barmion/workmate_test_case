import pytest

from performance_analyzer.main import main


def test_main_with_real_files(capsys, multiple_csv_path):
    """Main отрабатывает корректно."""
    with pytest.MonkeyPatch().context() as m:
        m.setattr('sys.argv', [
            'main.py',
            '--files', *map(str, multiple_csv_path),
            '--report', 'student-performance'
        ])
        main()
        captured = capsys.readouterr()
        output = captured.out

        assert 'Иванов Алексей' in output
        assert 'Морозова Екатерина' in output
        assert 'student_name' in output
        assert 'average_grade' in output


def test_main_file_not_found(capsys):
    """Ошибка при указании несуществующего файла."""
    with pytest.MonkeyPatch().context() as m:
        m.setattr('sys.argv', [
            'main.py',
            '--files', 'wrong.csv',
            '--report', 'student-performance'
        ])
        main()
        captured = capsys.readouterr()
        error_output = captured.out

        assert 'Ошибка' in error_output
        assert 'wrong.csv' in error_output


def test_main_wrong_report(capsys, multiple_csv_path):
    """Ошибка при указании несуществующего отчета."""
    with pytest.MonkeyPatch().context() as m:
        m.setattr('sys.argv', [
            'main.py',
            '--files', *map(str, multiple_csv_path),
            '--report', 'wrong-report'
        ])
        main()
        captured = capsys.readouterr()
        error_output = captured.out

        assert 'Ошибка' in error_output
        assert 'wrong-report' in error_output


def test_main_missing_arguments():
    """Ошибка, если не указать аргументы."""
    with pytest.MonkeyPatch().context() as m:
        m.setattr('sys.argv', ['main.py',])

        with pytest.raises(SystemExit):
            main()
