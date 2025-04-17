from dataclasses import dataclass


@dataclass
class Length:
    """
    Габаритные размеры приложения.

    - gap: отступы у каждого виджета, отступы от двух рядом стоящих виджетов
    складываются,
    - widget_height: высота виджета по умолчанию,
    - widget_width: длина виджета по умолчанию.
    """

    gap: int = 4
    widget_height: int = 40
    widget_width: int = 120
