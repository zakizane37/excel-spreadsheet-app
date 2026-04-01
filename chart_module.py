class ChartModule:
    """Модуль диаграмм и графиков."""

    def __init__(self):
        self.charts = []

    def create_chart(self, chart_type: str, data: list, title: str):
        """Создаёт диаграмму указанного типа."""
        chart = {"type": chart_type, "data": data, "title": title}
        self.charts.append(chart)
        print(f"Диаграмма '{title}' типа '{chart_type}' создана.")

    def get_available_types(self) -> list:
        """Возвращает список доступных типов диаграмм."""
        return ["bar", "line", "pie", "scatter"]
