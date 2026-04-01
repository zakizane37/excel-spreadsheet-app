class FormulaEngine:
    """Модуль вычисления формул."""

    def parse_formula(self, formula: str) -> str:
        """Разбирает строку формулы."""
        if formula.startswith("="):
            return formula[1:]
        return formula

    def calculate_sum(self, values: list) -> float:
        """Вычисляет сумму списка значений."""
        return sum(values)

    def calculate_average(self, values: list) -> float:
        """Вычисляет среднее значение списка."""
        if not values:
            raise ValueError("Список значений пуст")
        return sum(values) / len(values)
