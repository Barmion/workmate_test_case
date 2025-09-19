from abc import ABC, abstractmethod

from performance_analyzer.utils import PerfomanceRecord


class BaseReport(ABC):

    def __init__(self, data: list[PerfomanceRecord]) -> None:
        self.data = data

    @abstractmethod
    def get_report(self) -> list[str, float]:
        """Формирует отчет из заданных данных."""

    @abstractmethod
    def print_report(self) -> None:
        """Выводит отчет в терминал."""
