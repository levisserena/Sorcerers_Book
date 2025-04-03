from tkinter import Tk

from localization.localization import get_locales
from windows.main_window.window import window


def start():
    """Запустит главное окно приложения."""
    root = Tk()
    localization = get_locales()
    window(root, localization)
