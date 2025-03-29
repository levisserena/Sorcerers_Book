from tkinter.constants import  SUNKEN, RAISED, GROOVE, RIDGE
from tkinter import Tk, CENTER, Toplevel, StringVar, NORMAL, ACTIVE, DISABLED, BooleanVar
from tkinter.ttk import Button, Entry, Label, Radiobutton, Frame

from windows.util import dismiss
from windows.constants import Length as lng


def open_setting_window(localization):
    setting_window = Toplevel()
    setting_window.title(localization.title_window_setting)
    setting_window.geometry("600x600")
    setting_window.protocol(
        'WM_DELETE_WINDOW',  # перехватываем нажатие на крестик
        lambda: dismiss(setting_window),
    )
    setting_window.grab_set()  # захватываем пользовательский ввод
    setting_window.resizable(False, False)

    frame_localization = Frame(
        setting_window,
        borderwidth=2,
        relief=GROOVE,
    )
    frame_localization.place(
        x=lng.gap,
        y=lng.gap,
        height=lng.frame_localization_height,
        width=lng.frame_localization_width,
    )

    label_localization = Label(
        frame_localization,
        text='Выберете язык приложения:'
    )
    label_localization.place(
        x=lng.gap,
        y=lng.gap,
    )

    russian = 'Русский'
    english = 'English'

    language = BooleanVar(value=True)

    russian_button = Radiobutton(
        frame_localization,
        text=russian,
        value=True,
        variable=language,
    )
    russian_button.place(
        x=lng.gap,
        y=lng.gap+lng.widget_height,
    )

    russian_button = Radiobutton(
        frame_localization,
        text=english,
        value=False,
        variable=language,
    )
    russian_button.place(
        x=lng.gap+lng.widget_width,
        y=lng.gap+lng.widget_height,
    )

    label_local = Label(
        setting_window,
        textvariable=language
    )
    label_local.place(
        x=15,
        y=120,
    )