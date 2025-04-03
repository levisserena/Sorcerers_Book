from dataclasses import dataclass

from database.constant import LOCALIZATION_OPTIONS

@dataclass
class Length:
    """Габаритные размеры приложения."""

    main_window_height: int = 300
    main_window_width: int = 450

    size_window: str = '{}x{}'

    gap: int = 15
    widget_height: int = 30
    widget_width: int = 100
    entry_width: int = 370
    frame_localization_height: int = 45 * (len(LOCALIZATION_OPTIONS) + 1)
    frame_localization_width: int = 200
    frame_password_height: int = 250
    frame_password_width: int = 200
