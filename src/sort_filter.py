class SortFilter:
    """
    Модуль сортировки и фильтрации табличных данных.

    Реализует сортировку данных по одному или нескольким столбцам
    и фильтрацию строк по заданным условиям. Поддерживает автофильтр
    и пользовательские фильтры.

    Attributes:
        active_filters (dict): Словарь активных фильтров по столбцам.
        sort_history (list): История применённых сортировок.
    """

    def __init__(self):
        """
        Инициализирует модуль сортировки и фильтрации.

        Создаёт пустые структуры для хранения фильтров и истории сортировок.
        """
        self.active_filters = {}
        self.sort_history = []

    def sort_by_column(self, data: list, column: int, ascending: bool = True) -> list:
        """
        Сортирует данные по указанному столбцу.

        Args:
            data (list): Список строк таблицы для сортировки.
            column (int): Индекс столбца для сортировки (начиная с 0).
            ascending (bool): Направление сортировки. True — по возрастанию,
                False — по убыванию. По умолчанию True.

        Returns:
            list: Отсортированный список строк.

        Raises:
            IndexError: Если индекс столбца выходит за пределы таблицы.
        """
        sorted_data = sorted(data, key=lambda row: row[column], reverse=not ascending)
        self.sort_history.append({"column": column, "ascending": ascending})
        return sorted_data

    def apply_filter(self, column: int, condition: str, value) -> None:
        """
        Применяет фильтр к указанному столбцу.

        Args:
            column (int): Индекс столбца для фильтрации.
            condition (str): Условие фильтрации: '=', '>', '<', '>=', '<=', '!='.
            value: Значение для сравнения.

        Raises:
            ValueError: Если указано неподдерживаемое условие фильтрации.
        """
        supported = ["=", ">", "<", ">=", "<=", "!="]
        if condition not in supported:
            raise ValueError(f"Неподдерживаемое условие фильтрации: {condition}")
        self.active_filters[column] = {"condition": condition, "value": value}
        print(f"Фильтр применён к столбцу {column}: {condition} {value}")

    def clear_filter(self, column: int = None) -> None:
        """
        Снимает фильтр с указанного столбца или со всех столбцов.

        Args:
            column (int, optional): Индекс столбца. Если не указан,
                снимаются все фильтры.
        """
        if column is not None:
            self.active_filters.pop(column, None)
        else:
            self.active_filters.clear()
        print("Фильтры сняты.")

    def get_active_filters(self) -> dict:
        """
        Возвращает словарь активных фильтров.

        Returns:
            dict: Словарь активных фильтров в формате {столбец: условие}.
        """
        return self.active_filters
