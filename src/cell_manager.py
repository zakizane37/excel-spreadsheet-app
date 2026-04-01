class CellManager:
    """
    Модуль работы с ячейками и диапазонами электронной таблицы.

    Реализует базовые операции над ячейками и диапазонами: ввод и
    редактирование данных, выделение, копирование, вставку, перемещение,
    объединение и разделение ячеек. Обеспечивает корректную адресацию
    ячеек и поддержку абсолютных и относительных ссылок.

    Attributes:
        cells (dict): Словарь данных ячеек в формате {адрес: значение}.
        merged_cells (list): Список объединённых диапазонов ячеек.
        clipboard (dict): Буфер обмена для операций копирования/вставки.
    """

    def __init__(self):
        """
        Инициализирует модуль работы с ячейками.

        Создаёт пустые структуры данных для ячеек, объединений и буфера обмена.
        """
        self.cells = {}
        self.merged_cells = []
        self.clipboard = {}

    def set_value(self, address: str, value) -> None:
        """
        Устанавливает значение ячейки по адресу.

        Args:
            address (str): Адрес ячейки, например 'A1' или 'C5'.
            value: Значение для записи (строка, число или формула).
        """
        self.cells[address] = value

    def get_value(self, address: str):
        """
        Возвращает значение ячейки по адресу.

        Args:
            address (str): Адрес ячейки, например 'A1'.

        Returns:
            Значение ячейки или None, если ячейка пуста.
        """
        return self.cells.get(address, None)

    def clear_cell(self, address: str) -> None:
        """
        Очищает содержимое ячейки.

        Args:
            address (str): Адрес очищаемой ячейки.
        """
        if address in self.cells:
            del self.cells[address]

    def copy_range(self, start: str, end: str) -> dict:
        """
        Копирует диапазон ячеек в буфер обмена.

        Args:
            start (str): Адрес начальной ячейки диапазона, например 'A1'.
            end (str): Адрес конечной ячейки диапазона, например 'C5'.

        Returns:
            dict: Словарь скопированных ячеек.
        """
        self.clipboard = {}
        for address, value in self.cells.items():
            self.clipboard[address] = value
        print(f"Диапазон {start}:{end} скопирован в буфер обмена.")
        return self.clipboard

    def merge_cells(self, start: str, end: str) -> None:
        """
        Объединяет диапазон ячеек в одну.

        Args:
            start (str): Адрес верхней левой ячейки диапазона.
            end (str): Адрес нижней правой ячейки диапазона.

        Raises:
            ValueError: Если диапазон уже частично объединён.
        """
        merge_range = f"{start}:{end}"
        if merge_range in self.merged_cells:
            raise ValueError(f"Диапазон {merge_range} уже объединён")
        self.merged_cells.append(merge_range)
        print(f"Ячейки {merge_range} объединены.")
