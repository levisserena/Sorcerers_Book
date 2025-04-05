from dataclasses import dataclass


@dataclass
class Length:
    """Габаритные размеры приложения."""

    gap: int = 4
    widget_height: int = 40
    widget_width: int = 120
