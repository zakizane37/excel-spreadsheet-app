class MacroModule:
    """Модуль макросов и автоматизации."""

    def __init__(self):
        self.macros = {}

    def record_macro(self, name: str, actions: list):
        """Записывает макрос с заданным именем."""
        self.macros[name] = actions
        print(f"Макрос '{name}' записан ({len(actions)} действий).")

    def run_macro(self, name: str):
        """Запускает ранее записанный макрос."""
        if name not in self.macros:
            raise KeyError(f"Макрос '{name}' не найден")
        for action in self.macros[name]:
            print(f"Выполняется: {action}")
