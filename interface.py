class UserInterface:
    """Модуль пользовательского интерфейса."""

    def display_main_menu(self):
        """Отображает главное меню приложения."""
        print("=== Табличный процессор ===")
        print("1. Новый файл")
        print("2. Открыть файл")
        print("3. Сохранить файл")
        print("4. Выход")

    def get_user_input(self, prompt: str) -> str:
        """Получает ввод от пользователя."""
        return input(prompt)

    def display_result(self, message: str):
        """Отображает результат операции."""
        print(f"[OK] {message}")
