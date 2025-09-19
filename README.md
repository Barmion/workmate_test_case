# Скрипт для формирования отчетов

## Как запустить
Находясь в корневом каталоге проекта создайте виртуальное окружение и установите зависимости из файла requirements.txt
```
python -m venv venv

source venv/Scripts/activate

pip install -r requirements.txt
```

Выполните скрипт performance_analyzer.main с указанием аргументов --files (пусть к файлу csv, можно указать несколько через пробел) и --report (название отчета)

## Пример запуска
Находясь в корневом каталоге выполните команду
```
python -m performance_analyzer.main --files data/students1.csv data/students2.csv --report student-performance
```
Пример вывода
![Пример вывода](/example.JPG)

## Как добавить новый отчет
1. В каталоге performance_analyzer/reports создайте новый python-файл для отчета. Создайте класс, отнаследовавшись от класса BaseReport из файла performance_analyzer/reports/base_report.py. Реализуйте в своем классе методы get_report (формирование отчета из преобразованного csv-файла) и print_report (вывод отчета в терминал).
2. В файл performance_analyzer/reports/\_\_init__.py импортируйте свой класс, в словарь _REPORTS добавьте свой класс.

## Как запустить тесты
В головном каталоге выполните команду:
```
pytest
```