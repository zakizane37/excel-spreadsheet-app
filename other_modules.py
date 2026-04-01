class PivotTable:
    """
    Модуль сводных таблиц.

    Предоставляет инструменты для группировки, агрегации и анализа
    больших массивов данных. Позволяет динамически изменять структуру
    отчёта: переставлять поля строк, столбцов и значений.

    Attributes:
        source_data (list): Исходные данные для построения сводной таблицы.
        row_fields (list): Поля, используемые в качестве строк.
        column_fields (list): Поля, используемые в качестве столбцов.
        value_field (str): Поле, по которому производится агрегация.
        aggregation (str): Функция агрегации ('sum', 'avg', 'count').
    """

    def __init__(self, source_data: list):
        """
        Инициализирует модуль сводных таблиц.

        Args:
            source_data (list): Исходный набор данных для анализа.
        """
        self.source_data = source_data
        self.row_fields = []
        self.column_fields = []
        self.value_field = None
        self.aggregation = "sum"

    def set_row_fields(self, fields: list):
        """
        Устанавливает поля строк сводной таблицы.

        Args:
            fields (list): Список названий полей для строк.
        """
        self.row_fields = fields

    def set_value_field(self, field: str, aggregation: str = "sum"):
        """
        Устанавливает поле значений и функцию агрегации.

        Args:
            field (str): Название поля для агрегации.
            aggregation (str): Функция агрегации: 'sum', 'avg' или 'count'.

        Raises:
            ValueError: Если указана неподдерживаемая функция агрегации.
        """
        if aggregation not in ["sum", "avg", "count"]:
            raise ValueError(f"Неподдерживаемая функция агрегации: {aggregation}")
        self.value_field = field
        self.aggregation = aggregation


class DataValidation:
    """
    Модуль проверки данных.

    Обеспечивает задание правил ввода для ячеек: допустимые диапазоны
    чисел, списки допустимых значений, форматы дат. При нарушении правил
    отображает предупреждение или запрещает ввод.

    Attributes:
        rules (dict): Словарь правил валидации в формате {адрес: правило}.
    """

    def __init__(self):
        """
        Инициализирует модуль проверки данных.

        Создаёт пустой словарь правил валидации.
        """
        self.rules = {}

    def add_number_rule(self, address: str, min_val: float, max_val: float):
        """
        Добавляет правило для ограничения числового диапазона ввода.

        Args:
            address (str): Адрес ячейки или диапазона.
            min_val (float): Минимально допустимое значение.
            max_val (float): Максимально допустимое значение.

        Raises:
            ValueError: Если min_val больше max_val.
        """
        if min_val > max_val:
            raise ValueError("Минимальное значение не может превышать максимальное")
        self.rules[address] = {"type": "number", "min": min_val, "max": max_val}

    def add_list_rule(self, address: str, allowed_values: list):
        """
        Добавляет правило для ограничения ввода списком допустимых значений.

        Args:
            address (str): Адрес ячейки или диапазона.
            allowed_values (list): Список допустимых значений для ввода.
        """
        self.rules[address] = {"type": "list", "values": allowed_values}

    def validate(self, address: str, value) -> bool:
        """
        Проверяет соответствие значения правилу для указанной ячейки.

        Args:
            address (str): Адрес проверяемой ячейки.
            value: Проверяемое значение.

        Returns:
            bool: True если значение соответствует правилу, иначе False.
        """
        if address not in self.rules:
            return True
        rule = self.rules[address]
        if rule["type"] == "number":
            return rule["min"] <= float(value) <= rule["max"]
        if rule["type"] == "list":
            return value in rule["values"]
        return True


class Collaboration:
    """
    Модуль совместной работы.

    Реализует возможность одновременной работы нескольких пользователей
    над одним документом. Поддерживает разграничение прав доступа,
    комментарии к ячейкам и историю изменений.

    Attributes:
        users (dict): Словарь пользователей и их прав доступа.
        comments (dict): Словарь комментариев к ячейкам.
        change_history (list): История изменений документа.
    """

    def __init__(self):
        """
        Инициализирует модуль совместной работы.

        Создаёт пустые структуры для пользователей, комментариев и истории.
        """
        self.users = {}
        self.comments = {}
        self.change_history = []

    def add_user(self, username: str, role: str = "viewer"):
        """
        Добавляет пользователя с указанной ролью доступа.

        Args:
            username (str): Имя пользователя.
            role (str): Роль доступа — 'viewer' или 'editor'. По умолчанию 'viewer'.

        Raises:
            ValueError: Если указана неизвестная роль.
        """
        if role not in ["viewer", "editor"]:
            raise ValueError(f"Неизвестная роль: {role}")
        self.users[username] = role
        print(f"Пользователь '{username}' добавлен с ролью '{role}'.")

    def add_comment(self, address: str, author: str, text: str):
        """
        Добавляет комментарий к ячейке.

        Args:
            address (str): Адрес ячейки.
            author (str): Имя автора комментария.
            text (str): Текст комментария.
        """
        self.comments[address] = {"author": author, "text": text}
        print(f"Комментарий добавлен к ячейке {address}.")


class PrintExport:
    """
    Модуль печати и экспорта документов.

    Отвечает за настройку параметров печати: ориентация страницы, поля,
    масштаб, область печати, колонтитулы. Обеспечивает предварительный
    просмотр и отправку документа на печать, а также экспорт в PDF.

    Attributes:
        orientation (str): Ориентация страницы ('portrait' или 'landscape').
        scale (int): Масштаб печати в процентах.
        margins (dict): Поля страницы в сантиметрах.
    """

    def __init__(self):
        """
        Инициализирует модуль печати и экспорта.

        Устанавливает параметры страницы по умолчанию.
        """
        self.orientation = "portrait"
        self.scale = 100
        self.margins = {"top": 2.5, "bottom": 2.5, "left": 2.0, "right": 2.0}

    def set_orientation(self, orientation: str):
        """
        Устанавливает ориентацию страницы.

        Args:
            orientation (str): Ориентация — 'portrait' (книжная) или 'landscape' (альбомная).

        Raises:
            ValueError: Если указана неподдерживаемая ориентация.
        """
        if orientation not in ["portrait", "landscape"]:
            raise ValueError("Ориентация должна быть 'portrait' или 'landscape'")
        self.orientation = orientation

    def export_to_pdf(self, filepath: str) -> bool:
        """
        Экспортирует текущий документ в формат PDF.

        Args:
            filepath (str): Путь для сохранения PDF-файла.

        Returns:
            bool: True если экспорт выполнен успешно.

        Raises:
            ValueError: Если путь не заканчивается на '.pdf'.
        """
        if not filepath.endswith(".pdf"):
            raise ValueError("Путь должен заканчиваться на '.pdf'")
        print(f"Документ экспортирован в PDF: {filepath}")
        return True


class StatisticsModule:
    """
    Модуль статистики и анализа данных.

    Предоставляет расширенные инструменты анализа: описательная статистика,
    анализ «что если», подбор параметра. Интегрируется с модулем формул
    и диаграмм для наглядного представления результатов.

    Attributes:
        dataset (list): Текущий набор данных для анализа.
    """

    def __init__(self):
        """
        Инициализирует модуль статистики.

        Создаёт пустой набор данных для анализа.
        """
        self.dataset = []

    def load_data(self, data: list):
        """
        Загружает набор данных для анализа.

        Args:
            data (list): Список числовых значений для анализа.
        """
        self.dataset = data

    def get_descriptive_stats(self) -> dict:
        """
        Вычисляет описательную статистику по загруженным данным.

        Returns:
            dict: Словарь со значениями: min, max, mean, median, count.

        Raises:
            ValueError: Если набор данных пуст.
        """
        if not self.dataset:
            raise ValueError("Набор данных пуст")
        sorted_data = sorted(self.dataset)
        n = len(sorted_data)
        mean = sum(sorted_data) / n
        median = sorted_data[n // 2] if n % 2 != 0 else \
            (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
        return {
            "count": n,
            "min": sorted_data[0],
            "max": sorted_data[-1],
            "mean": mean,
            "median": median
        }

    def what_if_analysis(self, target: float, current: float, step: float) -> list:
        """
        Выполняет анализ «что если» для достижения целевого значения.

        Args:
            target (float): Целевое значение.
            current (float): Текущее значение.
            step (float): Шаг изменения значения.

        Returns:
            list: Список промежуточных значений от current до target.
        """
        results = []
        value = current
        while value < target:
            value += step
            results.append(round(value, 4))
        return results
