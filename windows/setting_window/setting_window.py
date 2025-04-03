from tkinter.constants import  SUNKEN, RAISED, GROOVE, RIDGE
from tkinter import Tk, CENTER, IntVar, Toplevel, StringVar, NORMAL, ACTIVE, DISABLED, BooleanVar
from tkinter.ttk import Button, Entry, Label, Radiobutton, Frame, Checkbutton

from database.constant import LOCALIZATION_OPTIONS
from database.crud import crud_setting
from localization.localization import LocalizationP
from windows.util import dismiss
from windows.constants import Length as lng


def open_setting_window(root: Tk, localization: type[LocalizationP]):
    """Откроет окно настроек."""
    all_settings = crud_setting.get_all_settings()

    localization_ = StringVar(value=all_settings['localization'])
    capital_ = BooleanVar(value=all_settings['capital'])
    numbers_ = BooleanVar(value=all_settings['numbers'])
    characters_ = BooleanVar(value=all_settings['characters'])
    min_ = IntVar(value=all_settings['min'])
    max_ = IntVar(value=all_settings['max'])

    setting_window = Toplevel(root)
    setting_window.title(localization.title_window_setting)
    setting_window.geometry(lng.size_window.format(
        600,
        400,
    ))
    setting_window.protocol(
        'WM_DELETE_WINDOW',  # перехватываем нажатие на крестик
        lambda: dismiss(setting_window),
    )
    setting_window.focus_force()
    setting_window.grab_set()  # захватываем пользовательский ввод
    setting_window.resizable(False, False)

    # Фрейм настройки локализацией.
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
        text=localization.text_label_localization,
    )
    label_localization.place(
        x=lng.gap,
        y=lng.gap,
    )

    for key, value in LOCALIZATION_OPTIONS.items():
        tag, name = value
        localization_button = Radiobutton(
            frame_localization,
            text=name,
            value=tag,
            variable=localization_,
        )
        localization_button.place(
            x=lng.gap,
            y=(lng.gap+lng.widget_height)*key,
        )

    # Фрейм настройки пароля.
    frame_password = Frame(
        setting_window,
        borderwidth=2,
        relief=GROOVE,
    )
    frame_password.place(
        x=lng.gap*2+lng.frame_localization_width,
        y=lng.gap,
        height=lng.frame_password_height,
        width=lng.frame_password_width,
    )

    label_password = Label(
        frame_password,
        text=localization.text_label_password,
    )
    label_password.place(
        x=lng.gap,
        y=lng.gap,
    )

    checkbutton = {
        'capital': capital_,
        'numbers': numbers_,
        'characters': characters_,
    }

    count = 1
    for name_, var in checkbutton.items():
        password_button = Checkbutton(
            frame_password,
            text=name_,
            variable=var,
        )
        password_button.place(
            x=lng.gap,
            y=(lng.gap+lng.widget_height)*count,
        )
        count += 1
