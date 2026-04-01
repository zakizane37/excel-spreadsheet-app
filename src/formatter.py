class Formatter:
    """
    Модуль форматирования данных и ячеек.

    Отвечает за визуальное оформление ячеек: шрифт, размер, цвет текста
    и фона, границы, выравнивание и числовые форматы. Поддерживает
    условное форматирование — автоматическое изменение оформления ячейки
    в зависимости от её значения.

    Attributes:
        formats (dict): Словарь форматов ячеек в формате {адрес: настройки}.
        conditional_rules (list): Список правил условного форматирования.
    """

    NUMBER_FORMATS = ["general", "number", "currency", "percent", "date", "time"]

    def __init__(self):
        """
        Инициализирует модуль форматирования.

        Создаёт пустые структуры для хранения форматов и правил условного форматирования.
        """
        self.formats = {}
        self.conditional_rules = []

    def set_font(self, address: str, font_name: str, size: int, bold: bool = False):
        """
        Устанавливает параметры шрифта для ячейки.

        Args:
            address (str): Адрес ячейки.
            font_name (str): Название шрифта, например 'Arial'.
            size (int): Размер шрифта в пунктах.
            bold (bool): Флаг жирного начертания. По умолчанию False.
        """
        if address not in self.formats:
            self.formats[address] = {}
        self.formats[address]["font"] = {
            "name": font_name, "size": size, "bold": bold
        }

    def set_background_color(self, address: str, color: str):
        """
        Устанавливает цвет фона ячейки.

        Args:
            address (str): Адрес ячейки.
            color (str): Цвет в формате HEX, например '#FFFF00'.

        Raises:
            ValueError: Если строка цвета не соответствует формату HEX.
        """
        if not color.startswith("#") or len(color) != 7:
            raise ValueError("Цвет должен быть в формате HEX, например '#FFFF00'")
        if address not in self.formats:
            self.formats[address] = {}
        self.formats[address]["background"] = color

    def set_number_format(self, address: str, fmt: str):
        """
        Устанавливает числовой формат ячейки.

        Args:
            address (str): Адрес ячейки.
            fmt (str): Тип формата: 'general', 'number', 'currency',
                'percent', 'date' или 'time'.

        Raises:
            ValueError: Если указан неподдерживаемый формат.
        """
        if fmt not in self.NUMBER_FORMATS:
            raise ValueError(f"Неподдерживаемый формат: {fmt}")
        if address not in self.formats:
            self.formats[address] = {}
        self.formats[address]["number_format"] = fmt

    def add_conditional_rule(self, cell_range: str, condition: str, fmt: dict):
        """
        Добавляет правило условного форматирования для диапазона ячеек.

        Args:
            cell_range (str): Диапазон ячеек, например 'A1:C10'.
            condition (str): Условие в виде строки, например '>100'.
            fmt (dict): Словарь с параметрами форматирования при выполнении условия.
        """
        rule = {"range": cell_range, "condition": condition, "format": fmt}
        self.conditional_rules.append(rule)
        print(f"Правило условного форматирования добавлено для {cell_range}.")
