class FormulaEngine:
    """
    Модуль вычисления формул и функций электронных таблиц.

    Осуществляет разбор, компиляцию и вычисление формул,
    введённых пользователем. Поддерживает стандартные математические,
    логические и статистические функции. Реализует механизм зависимостей
    между ячейками и автоматический пересчёт при изменении данных.

    Attributes:
        cell_data (dict): Словарь значений ячеек в формате {адрес: значение}.
        formula_cache (dict): Кэш результатов вычислений формул.
    """

    def __init__(self):
        """
        Инициализирует модуль вычисления формул.

        Создаёт пустой словарь данных ячеек и кэш формул.
        """
        self.cell_data = {}
        self.formula_cache = {}

    def parse_formula(self, formula: str) -> str:
        """
        Разбирает строку формулы и возвращает выражение для вычисления.

        Args:
            formula (str): Строка формулы, начинающаяся с символа '='.

        Returns:
            str: Выражение без префикса '=', готовое к вычислению.
        """
        if formula.startswith("="):
            return formula[1:]
        return formula

    def calculate_sum(self, values: list) -> float:
        """
        Вычисляет сумму списка числовых значений.

        Args:
            values (list): Список числовых значений ячеек.

        Returns:
            float: Сумма всех значений в списке.

        Raises:
            TypeError: Если список содержит нечисловые значения.
        """
        return sum(values)

    def calculate_average(self, values: list) -> float:
        """
        Вычисляет среднее арифметическое списка значений.

        Args:
            values (list): Список числовых значений ячеек.

        Returns:
            float: Среднее арифметическое значений.

        Raises:
            ValueError: Если список значений пуст.
        """
        if not values:
            raise ValueError("Список значений пуст")
        return sum(values) / len(values)

    def calculate_max(self, values: list) -> float:
        """
        Возвращает максимальное значение из списка.

        Args:
            values (list): Список числовых значений ячеек.

        Returns:
            float: Максимальное значение в списке.

        Raises:
            ValueError: Если список значений пуст.
        """
        if not values:
            raise ValueError("Список значений пуст")
        return max(values)

    def calculate_min(self, values: list) -> float:
        """
        Возвращает минимальное значение из списка.

        Args:
            values (list): Список числовых значений ячеек.

        Returns:
            float: Минимальное значение в списке.

        Raises:
            ValueError: Если список значений пуст.
        """
        if not values:
            raise ValueError("Список значений пуст")
        return min(values)

    def set_cell_value(self, address: str, value):
        """
        Устанавливает значение ячейки по её адресу.

        Args:
            address (str): Адрес ячейки в формате 'A1', 'B2' и т.д.
            value: Значение для записи в ячейку.
        """
        self.cell_data[address] = value
        if address in self.formula_cache:
            del self.formula_cache[address]

    def get_cell_value(self, address: str):
        """
        Возвращает значение ячейки по её адресу.

        Args:
            address (str): Адрес ячейки в формате 'A1', 'B2' и т.д.

        Returns:
            Значение ячейки или None, если ячейка не найдена.
        """
        return self.cell_data.get(address, None)
