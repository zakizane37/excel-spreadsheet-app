class SheetManager:
    """
    Модуль управления листами электронной таблицы.

    Обеспечивает создание, переименование, копирование, перемещение
    и удаление листов в рамках одного файла. Реализует навигацию
    между листами и поддержку межлистовых формульных ссылок.

    Attributes:
        sheets (list): Список листов документа.
        active_sheet (str): Имя активного (текущего) листа.
    """

    def __init__(self):
        """
        Инициализирует модуль управления листами.

        Создаёт документ с одним листом по умолчанию — 'Лист1'.
        """
        self.sheets = ["Лист1"]
        self.active_sheet = "Лист1"

    def add_sheet(self, name: str) -> bool:
        """
        Добавляет новый лист с указанным именем.

        Args:
            name (str): Имя нового листа.

        Returns:
            bool: True если лист успешно создан.

        Raises:
            ValueError: Если лист с таким именем уже существует.
        """
        if name in self.sheets:
            raise ValueError(f"Лист с именем '{name}' уже существует")
        self.sheets.append(name)
        print(f"Лист '{name}' добавлен.")
        return True

    def rename_sheet(self, old_name: str, new_name: str) -> bool:
        """
        Переименовывает лист.

        Args:
            old_name (str): Текущее имя листа.
            new_name (str): Новое имя листа.

        Returns:
            bool: True если переименование выполнено успешно.

        Raises:
            KeyError: Если лист с именем old_name не найден.
            ValueError: Если лист с именем new_name уже существует.
        """
        if old_name not in self.sheets:
            raise KeyError(f"Лист '{old_name}' не найден")
        if new_name in self.sheets:
            raise ValueError(f"Лист с именем '{new_name}' уже существует")
        index = self.sheets.index(old_name)
        self.sheets[index] = new_name
        if self.active_sheet == old_name:
            self.active_sheet = new_name
        return True

    def delete_sheet(self, name: str) -> bool:
        """
        Удаляет лист по имени.

        Args:
            name (str): Имя удаляемого листа.

        Returns:
            bool: True если лист успешно удалён.

        Raises:
            KeyError: Если лист с указанным именем не найден.
            ValueError: Если попытка удалить единственный оставшийся лист.
        """
        if name not in self.sheets:
            raise KeyError(f"Лист '{name}' не найден")
        if len(self.sheets) == 1:
            raise ValueError("Нельзя удалить единственный лист документа")
        self.sheets.remove(name)
        if self.active_sheet == name:
            self.active_sheet = self.sheets[0]
        return True

    def get_sheet_list(self) -> list:
        """
        Возвращает список имён всех листов документа.

        Returns:
            list: Список строк с именами листов.
        """
        return self.sheets
