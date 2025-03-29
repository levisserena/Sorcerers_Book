from dataclasses import dataclass


@dataclass
class Length:
    """Габаритные размеры приложения."""

    main_window_height = 300
    main_window_width = 450

    gap = 15
    widget_height = 30
    widget_width = 100
    entry_width = 370
    frame_localization_height = 90
    frame_localization_width = 200
