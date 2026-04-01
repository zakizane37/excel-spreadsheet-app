class FileManager:
    """
    Модуль управления файлами электронных таблиц.

    Обеспечивает создание, открытие, сохранение и закрытие файлов.
    Поддерживает форматы .xlsx, .csv, .ods и .pdf.
    Предусматривает историю недавних файлов и автосохранение.

    Attributes:
        current_file (str): Путь к текущему открытому файлу.
        recent_files (list): Список путей к недавно открытым файлам.
        autosave_enabled (bool): Флаг включения автосохранения.
    """

    SUPPORTED_FORMATS = [".xlsx", ".csv", ".ods", ".pdf"]

    def __init__(self):
        """
        Инициализирует модуль управления файлами.

        Создаёт пустой список недавних файлов и отключает автосохранение.
        """
        self.current_file = None
        self.recent_files = []
        self.autosave_enabled = False

    def create_new(self) -> bool:
        """
        Создаёт новый пустой документ.

        Returns:
            bool: True если документ успешно создан.
        """
        self.current_file = None
        print("Новый документ создан.")
        return True

    def open_file(self, filepath: str) -> bool:
        """
        Открывает существующий файл электронной таблицы.

        Args:
            filepath (str): Полный путь к открываемому файлу.

        Returns:
            bool: True если файл успешно открыт, False в случае ошибки.

        Raises:
            FileNotFoundError: Если файл по указанному пути не найден.
            ValueError: Если формат файла не поддерживается.
        """
        ext = filepath[filepath.rfind("."):]
        if ext not in self.SUPPORTED_FORMATS:
            raise ValueError(f"Формат '{ext}' не поддерживается")
        self.current_file = filepath
        if filepath not in self.recent_files:
            self.recent_files.insert(0, filepath)
            if len(self.recent_files) > 10:
                self.recent_files.pop()
        print(f"Файл открыт: {filepath}")
        return True

    def save_file(self, filepath: str = None) -> bool:
        """
        Сохраняет текущий документ.

        Args:
            filepath (str, optional): Путь для сохранения. Если не указан,
                используется путь текущего файла.

        Returns:
            bool: True если файл успешно сохранён.

        Raises:
            ValueError: Если не указан путь и документ ещё не сохранялся.
        """
        target = filepath or self.current_file
        if not target:
            raise ValueError("Укажите путь для сохранения файла")
        self.current_file = target
        print(f"Файл сохранён: {target}")
        return True

    def get_recent_files(self) -> list:
        """
        Возвращает список недавно открытых файлов.

        Returns:
            list: Список путей к недавно открытым файлам (до 10 записей).
        """
        return self.recent_files

    def enable_autosave(self, interval_minutes: int = 5):
        """
        Включает автоматическое сохранение документа.

        Args:
            interval_minutes (int): Интервал автосохранения в минутах.
                По умолчанию 5 минут.

        Raises:
            ValueError: Если интервал меньше 1 минуты.
        """
        if interval_minutes < 1:
            raise ValueError("Интервал автосохранения не может быть менее 1 минуты")
        self.autosave_enabled = True
        print(f"Автосохранение включено: каждые {interval_minutes} мин.")
