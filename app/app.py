from tkinter.constants import  SUNKEN, RAISED, GROOVE, RIDGE
from tkinter import Tk, CENTER, IntVar, Toplevel, StringVar, NORMAL, ACTIVE, DISABLED, BooleanVar
from tkinter.ttk import Button, Entry, Label, Radiobutton, Frame, Checkbutton

from app.constants.constants import ICONBITMAP
from app.constants.config import Config, DefaultConfig
from app.constants.length import Length
from app.constants.localization import get_locales, LOCALIZATION_OPTIONS
from app.crud.config import crud_config
from app.crud.payload import crud_payload
from app.mixin import ButtonMixin, EntryMixin, LabelMixin, RadiobuttonMixin, WindowMixin


class SorcerersBool(
    ButtonMixin,
    EntryMixin,
    LabelMixin,
    RadiobuttonMixin,
    WindowMixin,
):
    """Описывает работу окон."""

    def __init__(self):
        """
        default_config: конфигурация приложения по умолчанию.
        crud_payload: управление таблицей с полезной нагрузкой.
        crud_config: управление таблицей с конфигурацией приложения.
        root: экземпляр класса из библиотеки tkinter - основа приложения.
        """
        self.default_config = DefaultConfig.get_default_config()
        self.crud_payload = crud_payload
        self.crud_config = crud_config
        self.root = Tk()

    def start(self):
        """
        Запустит цепочку команд:
        - создаст базу данных (если её нет) и таблицу в ней для полезной нагрузки (если её нет),
        - создаст таблицу для хранения конфигурации приложения (если её нет),
        - заполнит таблицу для хранения конфигурации приложения значениями по умолчанию,
          если она ещё не заполнена.
        - выберет локализацию приложения,
        - установит все переменные, которые будут отслеживаться приложением,
        - запустит главное окно приложения.
        """
        crud_payload.create_db()
        crud_config.create_db()
        crud_config.create_rows_in_db(self.default_config)
        self.localization = get_locales()
        self.install_everything_variable()
        self.open_window_main()

    def install_everything_variable(self):
        """Установит все переменные, которые будут отслеживаться приложением"""
        self.search_by_input = StringVar()

        config_db = crud_config.get_all_settings()
        self.config_localization = StringVar(value=config_db[Config.localization_app])
        self.config_capital_letters = BooleanVar(value=config_db[Config.capital_letters])
        self.config_numbers = BooleanVar(value=config_db[Config.numbers])
        self.config_characters = BooleanVar(value=config_db[Config.characters])
        self.config_min_length_password = IntVar(value=config_db[Config.min_length_password])
        self.config_max_length_password = IntVar(value=config_db[Config.max_length_password])

    def open_window_main(self):
        """Откроет главное окно, описывает его логику работы."""
        window = self.configure_window(
            self.root,
            self.localization.title_window_main,
            iconbitmap=ICONBITMAP,
        )
        self.set_up_column_and_row_settings(
            window=window,
            number_row=3,
            number_column=4,
        )
        entry = self.add_entry_field(
            master=window,
            textvariable=self.search_by_input,
            row=0,
            column=0,
            columnspan=3,
        )
        lable = self.add_label(
            master=window,
            row=1,
            column=0,
            columnspan=3,
            text=self.search_by_input.get()
        )
        data_button = [
            {
                'text': self.localization.button_create,
                'row': 2,
                'column': 0,
                'command': lambda: print(self.localization.button_create),
            },
            {
                'text': self.localization.button_updata,
                'row': 2,
                'column': 1,
                'command': lambda: print(self.localization.button_updata),
            },
            {
                'text': self.localization.button_all_note,
                'row': 2,
                'column': 2,
                'command': lambda: print(self.localization.button_all_note),
            },
            {
                'text': self.localization.button_search,
                'row': 0,
                'column': 3,
                'command': lambda: print(self.localization.button_search),
            },
            {
                'text': self.localization.button_copy,
                'row': 1,
                'column': 3,
                'command': lambda: print(self.localization.button_copy),
            },
            {
                'text': self.localization.button_config,
                'row': 2,
                'column': 3,
                'command': lambda: self.open_config_window(window),
            },
        ]
        for button in data_button:
            self.add_button(master=window, **button)
        window.mainloop()

    def open_config_window(self, window_master):
        """Откроет окно настроек."""
        window = Toplevel(window_master)
        self.configure_window(
            window=window,
            title=self.localization.title_window_config,
            grab_set=True,
            focus_force=True,
        )
        self.set_up_column_and_row_settings(
            window=window,
            number_row=2,
            number_column=2,
        )
        for row, value in enumerate(LOCALIZATION_OPTIONS):
            tag, name = value
            self.add_radiobutton(
                master=window,
                text=name,
                value=tag,
                variable=self.config_localization,
                row=row,
                column=0,
            )
