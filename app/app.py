from tkinter import Tk, CENTER, IntVar, Toplevel, StringVar, NORMAL, ACTIVE, DISABLED, BooleanVar, W, E, END, RIGHT
from tkinter.constants import  SUNKEN, RAISED, GROOVE, RIDGE
from tkinter.ttk import Button, Entry, Label, Radiobutton, Frame, Checkbutton, Style
from tkinter.messagebox import OK, INFO, showerror, showwarning, showinfo

from app.utils.password_generator import generate_password
from app.constants.constants import ICONBITMAP, FONT_REGULAR, FONT_UNDERLINED
from app.constants.config import Config, DefaultConfig
from app.constants.length import Length
from app.constants.constants import TAG_DEFAULT_LOCALIZATION
from app.constants.localization import get_locales, LOCALIZATION_OPTIONS
from app.crud.config import crud_config
from app.crud.payload import crud_payload
from app.mixin import (
    ButtonMixin,
    CheckbuttonMixin,
    EntryMixin,
    FrameMixin,
    LabelMixin,
    RadiobuttonMixin,
    SpinboxMixin,
    TextMixin,
    WindowMixin,
)


class SorcerersBook(
    ButtonMixin,
    CheckbuttonMixin,
    EntryMixin,
    FrameMixin,
    LabelMixin,
    RadiobuttonMixin,
    SpinboxMixin,
    TextMixin,
    WindowMixin,
):
    """Описывает работу окон."""

    def __init__(self):
        """
        default_config: конфигурация приложения по умолчанию.
        config_field: название полей в БД
        crud_payload: управление таблицей с полезной нагрузкой.
        crud_config: управление таблицей с конфигурацией приложения.
        root: экземпляр класса из библиотеки tkinter - основа приложения.
        style: отвечает за стиль приложения.
        """
        self.default_config = DefaultConfig.get_default_config()
        self.config_field = Config
        self.crud_payload = crud_payload
        self.crud_config = crud_config
        self.root = Tk()
        self.style = Style()

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
        self.style.configure('.', font=FONT_REGULAR)
        self.open_main_window()

    def install_everything_variable_for_main_window(self) -> None:
        """Установит переменные, которые будут отслеживаться приложением, для главного окна."""
        self.search_by_input = StringVar()

    def install_everything_variable_for_create_window(self) -> None:
        """
        Установит переменные, которые будут отслеживаться приложением,
        для окна создания новой записи в БД.
        """
        self.slug_field = StringVar()
        self.password_field = StringVar()

    def install_everything_variable_for_config_window(self) -> None:
        """Установит переменные, которые будут отслеживаться приложением, для окна конфигурации."""

        config_db = crud_config.get_all_settings()
        self.config_localization_app = StringVar(
            value=config_db[self.config_field.localization_app],
        )
        self.config_capital_letters = BooleanVar(
            value=config_db[self.config_field.capital_letters],
        )
        self.config_numbers = BooleanVar(
            value=config_db[self.config_field.numbers],
        )
        self.config_characters = BooleanVar(
            value=config_db[self.config_field.characters],
        )
        self.config_min_length_password = IntVar(
            value=config_db[self.config_field.min_length_password],
        )
        self.config_max_length_password = IntVar(
            value=config_db[self.config_field.max_length_password],
        )

    def open_main_window(self) -> None:
        """Откроет главное окно, описывает его логику работы."""
        self.install_everything_variable_for_main_window()

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
            text=self.search_by_input.get(),
            borderwidth=2,
            relief=SUNKEN,
        )
        data_button = (
            {
                'text': self.localization.button_create,
                'row': 2,
                'column': 0,
                'command': lambda: self.open_create_window(window),
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
        )
        for button in data_button:
            self.add_button(master=window, **button)
        window.mainloop()

    def open_create_window(self, window_master) -> None:
        """Откроет окно создания новой записи в БД."""
        self.install_everything_variable_for_create_window()

        window = Toplevel(window_master)
        self.configure_window(
            window=window,
            title='Создать новую запись',
            grab_set=True,
            focus_force=True,
        )
        self.set_up_column_and_row_settings(
            window=window,
            number_row=7,
            number_column=4,
        )

        data_label = (
            {
                'text': 'Короткое название (сохранится без пробелов по краям):',
                'row': 0,
            },
            {
                'text': 'Более подробное описание, чтоб не забыть, про что это вообще:',
                'row': 2,
            },
            {
                'text': 'Пароль, для указанного артефакта (сохранится без пробелов):',
                'row': 4,
            },
        )
        for label in data_label:
            self.add_label(
                master=window,
                column=0,
                columnspan=4,
                **label,
            )

        data_entry = (
            {
                'textvariable': self.slug_field,
                'row': 1,
            },
            {
                'textvariable': self.password_field,
                'row': 5,
            },
        )
        for entry in data_entry:
            self.add_entry_field(
                master=window,
                column=0,
                columnspan=4,
                **entry,
            )

        text_field = self.add_text_field(
            master=window,
            row=3,
            column=0,
            columnspan=4,
        )

        def set_value_entry_password():
            config_db = crud_config.get_all_settings()
            self.password_field.set(generate_password(
                min_range_pass=config_db[self.config_field.min_length_password],
                max_range_pass=config_db[self.config_field.max_length_password],
                number=int(config_db[self.config_field.numbers]),
                characters=int(config_db[self.config_field.characters]),
                capital_letters=int(config_db[self.config_field.capital_letters]),
            ))

        data_button = (
            {
                'text': 'Сгенерировать',
                'command': lambda: set_value_entry_password(),
                'column': 0,
            },
            {
                'text': 'Создать',
                'command': lambda: self.create_entry_in_database(
                    slug=self.slug_field.get(),
                    description=text_field.get(),
                    password=self.password_field.get(),
                    window=window,
                ),
                'column': 2,
            },
            {
                'text': 'Отмена',
                'command': lambda: self.dismiss(window),
                'column': 3,
            },
        )
        for button in data_button:
            self.add_button(
                master=window,
                row=6,
                **button,
            )

    def open_config_window(self, window_master) -> None:
        """Откроет окно настроек."""
        self.install_everything_variable_for_config_window()

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
            number_column=4,
        )
        frame_localization = self.add_frame(
            master=window,
            row=0,
            column=0,
        )
        frame_password = self.add_frame(
            master=window,
            row=0,
            column=1,
            columnspan=3,
        )

        data_label = (
            {
                'master': frame_localization,
                'text': self.localization.text_label_localization,
                'row': 0,
                'column': 0,
            },
            {
                'master': frame_password,
                'text': self.localization.text_label_password,
                'row': 0,
                'column': 0,
            },
            {
                'master': frame_password,
                'text': self.localization.label_min_length_password,
                'row': 1,
                'column': 0,
            },
            {
                'master': frame_password,
                'text': self.localization.label_max_length_password,
                'row': 2,
                'column': 0,
            },
        )
        for label in data_label:
            self.add_label(**label)

        for row, value in enumerate(LOCALIZATION_OPTIONS, 1):
            tag, name = value
            self.add_radiobutton(
                master=frame_localization,
                text=name,
                value=tag,
                variable=self.config_localization_app,
                row=row,
                column=0,
            )

        data_checkbutton = (
            {
                'text': self.localization.checkbutton_capital_letters,
                'variable': self.config_capital_letters,
            },
            {
                'text': self.localization.checkbutton_numbers,
                'variable': self.config_numbers,
            },
            {
                'text': self.localization.checkbutton_characters,
                'variable': self.config_characters,
            },
        )
        for row, checkbutton in enumerate(data_checkbutton, 3):
            self.add_checkbutton(
                master=frame_password,
                row=row,
                column=0,
                **checkbutton,
            )

        def update_limits(*args):
            """
            Обновляет допустимые диапазоны для обоих Spinbox,
            чтобы минимальная длина пароля не была больше максимальной.
            """
            try:
                spinbox_max_length_password.config(from_=int(spinbox_min_length_password.get()))
                spinbox_min_length_password.config(to=int(spinbox_max_length_password.get()))
            except ValueError:
                pass

        spinbox_min_length_password = self.add_spinbox(
            master=frame_password,
            textvariable=self.config_min_length_password,
            from_=8,
            to=100,
            row=1,
            column=1,
            command=update_limits,
        )
        spinbox_max_length_password = self.add_spinbox(
            master=frame_password,
            textvariable=self.config_max_length_password,
            from_=8,
            to=100,
            row=2,
            column=1,
            command=update_limits,
        )
        # <ButtonRelease-1> отслеживает момент, когда пользователь отпускает левую кнопку мыши
        spinbox_min_length_password.bind('<ButtonRelease-1>', update_limits)
        spinbox_max_length_password.bind('<ButtonRelease-1>', update_limits)

        data_button = (
            {
                'text': self.localization.button_config_about,
                'column': 0,
                'command': lambda: self.open_about_window(window),
            },
            {
                'text': self.localization.button_config_apply,
                'column': 2,
                'command': lambda: self.save_config(window),
            },
            {
                'text': self.localization.button_config_cancel,
                'column': 3,
                'command': lambda: self.dismiss(window),
            },
        )
        for button in data_button:
            self.add_button(master=window, row=1, **button)

    def open_about_window(self, window_master) -> None:
        """Откроет окно с информацией о проекте."""
        window = Toplevel(window_master)
        self.configure_window(
            window=window,
            title=self.localization.title_window_about,
            grab_set=True,
            focus_force=True,
        )
        data_label = (
            {
                'row': 0,
                'text': self.localization.text_for_about_windows,
            },
            {
                'row': 2,
                'text': self.localization.text_for_about_windows_signature,
                'sticky': E,
            },
        )
        for label in data_label:
            self.add_label(
                master=window,
                column=0,
                columnspan=3,
                **label,
            )
        self.add_link(
            master=window,
            row=1,
            column=0,
            columnspan=3,
            text=self.localization.text_for_about_windows_link,
        )
        self.add_button(
            master=window,
            text=self.localization.button_config_about_close,
            command=lambda: self.dismiss(window),
            row=3,
            column=2,
        )

    def create_entry_in_database(
        self, slug: str, password: str, description: str, window: Toplevel,
    ) -> None:
        """
        Создаст новую запись в базе данных.
        В конце закроет окно для создания записи в БД.

        - slug: значение для поля slug,
        - password: значение для поля password,
        - description: значение для поля description,
        - window: окно, которое необходимо закрыть по завершению.
        """
        if not slug:
            showerror(title='Исправьте ввод', message='Короткое название не может быть пустым')
        elif self.crud_payload.get_by_slug_or_none(slug=slug):
            showerror(
                title='Исправьте ввод',
                message='Такое короткое название уже есть в базе данных',
            )
        elif not password:
            showerror(title='Исправьте ввод', message='Пароль не может быть пустым')
        else:
            slug_corrected = slug.strip()
            password_corrected = password.strip().replace(' ', '')
            self.crud_payload.create_entry(
                slug=slug_corrected,
                description=description,
                password=password_corrected,
            )
            self.dismiss(window)

    def save_config(self, window) -> None:
        """
        Обрабатывает работу кнопки "Принять" окна конфигурации.

        - Проверит валидность данных.
        - Сохранит изменения настроек в БД,
        - Закроет окно конфигурации.
        """
        self.validation_config()
        self.crud_config.update_all(
            {
                self.config_field.localization_app: self.config_localization_app.get(),
                self.config_field.capital_letters: self.config_capital_letters.get(),
                self.config_field.numbers: self.config_numbers.get(),
                self.config_field.characters: self.config_characters.get(),
                self.config_field.min_length_password: self.config_min_length_password.get(),
                self.config_field.max_length_password: self.config_max_length_password.get(),
            }
        )
        self.dismiss(window)

    def validation_config(self) -> None:
        """
        Валидатор конфигурации.

        Если, по какой-либо причине, данные конфигурации для записи в БД будут не валидны,
        принудительно сделает их валидными, например, поставит значения по умолчанию.
        """
        if self.config_localization_app.get() not in [tag for tag, _ in LOCALIZATION_OPTIONS]:
            self.config_localization_app.set(
                self.default_config[self.config_field.localization_app]
            )
        for value, field in (
            (self.config_capital_letters, self.config_field.capital_letters),
            (self.config_numbers, self.config_field.numbers),
            (self.config_characters, self.config_field.characters),
        ):
            if not isinstance(value.get(), bool):
                value.set(self.default_config[field])
        if self.config_min_length_password.get() > (max_ := self.config_max_length_password.get()):
            self.config_min_length_password.set(max_)
