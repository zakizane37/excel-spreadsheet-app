class ChartModule:
    """
    Модуль построения диаграмм и графиков.

    Позволяет строить графические представления табличных данных:
    гистограммы, линейные, круговые, точечные и другие типы диаграмм.
    Обеспечивает настройку заголовков, легенды, осей и цветовых схем.

    Attributes:
        charts (list): Список созданных диаграмм.
        default_colors (list): Набор цветов по умолчанию для диаграмм.
    """

    def __init__(self):
        """
        Инициализирует модуль диаграмм.

        Создаёт пустой список диаграмм и задаёт цветовую схему по умолчанию.
        """
        self.charts = []
        self.default_colors = ["#4472C4", "#ED7D31", "#A9D18E", "#FF0000"]

    def create_chart(self, chart_type: str, data: list, title: str) -> dict:
        """
        Создаёт диаграмму указанного типа на основе переданных данных.

        Args:
            chart_type (str): Тип диаграммы ('bar', 'line', 'pie', 'scatter').
            data (list): Данные для построения диаграммы.
            title (str): Заголовок диаграммы.

        Returns:
            dict: Словарь с параметрами созданной диаграммы.

        Raises:
            ValueError: Если указан неподдерживаемый тип диаграммы.
        """
        if chart_type not in self.get_available_types():
            raise ValueError(f"Неподдерживаемый тип диаграммы: {chart_type}")
        chart = {"type": chart_type, "data": data, "title": title}
        self.charts.append(chart)
        print(f"Диаграмма '{title}' типа '{chart_type}' создана.")
        return chart

    def get_available_types(self) -> list:
        """
        Возвращает список доступных типов диаграмм.

        Returns:
            list: Список строк с названиями поддерживаемых типов диаграмм.
        """
        return ["bar", "line", "pie", "scatter"]

    def delete_chart(self, title: str) -> bool:
        """
        Удаляет диаграмму по её заголовку.

        Args:
            title (str): Заголовок удаляемой диаграммы.

        Returns:
            bool: True если диаграмма найдена и удалена, иначе False.
        """
        for chart in self.charts:
            if chart["title"] == title:
                self.charts.remove(chart)
                return True
        return False

    def get_chart_count(self) -> int:
        """
        Возвращает количество созданных диаграмм.

        Returns:
            int: Количество диаграмм в текущем документе.
        """
        return len(self.charts)
