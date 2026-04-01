class MacroModule:
    """
    Модуль макросов и автоматизации.

    Позволяет записывать и воспроизводить последовательности действий
    пользователя (макросы), а также выполнять пользовательские скрипты.
    Обеспечивает назначение макросов на кнопки и сочетания клавиш.

    Attributes:
        macros (dict): Словарь записанных макросов в формате {имя: список действий}.
        hotkeys (dict): Словарь назначенных горячих клавиш в формате {клавиши: имя макроса}.
    """

    def __init__(self):
        """
        Инициализирует модуль макросов.

        Создаёт пустые словари макросов и горячих клавиш.
        """
        self.macros = {}
        self.hotkeys = {}

    def record_macro(self, name: str, actions: list):
        """
        Записывает макрос с заданным именем и набором действий.

        Args:
            name (str): Уникальное имя макроса.
            actions (list): Список действий, составляющих макрос.

        Raises:
            ValueError: Если список действий пуст.
        """
        if not actions:
            raise ValueError("Список действий не может быть пустым")
        self.macros[name] = actions
        print(f"Макрос '{name}' записан ({len(actions)} действий).")

    def run_macro(self, name: str):
        """
        Запускает ранее записанный макрос по имени.

        Args:
            name (str): Имя макроса для запуска.

        Raises:
            KeyError: Если макрос с указанным именем не найден.
        """
        if name not in self.macros:
            raise KeyError(f"Макрос '{name}' не найден")
        for action in self.macros[name]:
            print(f"Выполняется: {action}")

    def assign_hotkey(self, keys: str, macro_name: str):
        """
        Назначает горячую клавишу для запуска макроса.

        Args:
            keys (str): Сочетание клавиш, например 'Ctrl+Shift+M'.
            macro_name (str): Имя макроса, который будет запущен.

        Raises:
            KeyError: Если макрос с указанным именем не существует.
        """
        if macro_name not in self.macros:
            raise KeyError(f"Макрос '{macro_name}' не найден")
        self.hotkeys[keys] = macro_name
        print(f"Горячая клавиша '{keys}' назначена макросу '{macro_name}'.")

    def delete_macro(self, name: str) -> bool:
        """
        Удаляет макрос по имени.

        Args:
            name (str): Имя удаляемого макроса.

        Returns:
            bool: True если макрос найден и удалён, иначе False.
        """
        if name in self.macros:
            del self.macros[name]
            return True
        return False

    def get_macro_list(self) -> list:
        """
        Возвращает список имён всех записанных макросов.

        Returns:
            list: Список строк с именами макросов.
        """
        return list(self.macros.keys())
