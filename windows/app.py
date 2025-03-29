from tkinter import Tk
from typing import Type

from localization.localization import LocalizationP
from windows.main_window.window import window


def start(localization: type[LocalizationP]):
    """Запустит главное окно приложения."""
    root = Tk()
    window(root, localization)
