import argparse

from performance_analyzer.reports import get_report_class
from performance_analyzer.utils import read_csv_files


def parse_script_args() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description='Формирование отчетов успеваимости',
    )
    parser.add_argument(
        '-f',
        '--files',
        nargs='+',
        required=True,
        help='Путь к csv-файлам (можно указать несколько через пробел)',
    )
    parser.add_argument(
        '-r',
        '--report',
        required=True,
        help='Название отчета',
    )
    return parser.parse_args()


def main():
    args = parse_script_args()
    try:
        data = read_csv_files(args.files)
        report_class = get_report_class(args.report)
        report = report_class(data)
        report.print_report()
    except Exception as e:
        print(f'Ошибка {e}')


if __name__ == '__main__':
    main()
