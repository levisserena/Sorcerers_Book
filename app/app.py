from tkinter import BooleanVar, IntVar, StringVar, Tk, Toplevel, Variable
from tkinter.constants import E, SUNKEN
from tkinter.ttk import Style
from tkinter.messagebox import askyesno, showerror

from app.constants.config import Config, DefaultConfig
from app.constants.constants import ICONBITMAP, FONT_REGULAR
from app.constants.database import ConstantDataBase
from app.constants.localization import get_locales, LOCALIZATION_OPTIONS
from app.crud.config import crud_config
from app.crud.payload import crud_payload
from app.mixin import (
    ButtonMixin,
    CheckbuttonMixin,
    EntryMixin,
    FrameMixin,
    LabelMixin,
    ListboxMixin,
    RadiobuttonMixin,
    SpinboxMixin,
    TextMixin,
    WindowMixin,
)
from app.utils.password_generator import generate_password


class SorcerersBook(
    ButtonMixin,
    CheckbuttonMixin,
    EntryMixin,
    FrameMixin,
    LabelMixin,
    ListboxMixin,
    RadiobuttonMixin,
    SpinboxMixin,
    TextMixin,
    WindowMixin,
):
    """Описывает работу окон."""

    def __init__(self):
        """
        Атрибуты класса при инициации:
        - default_config: конфигурация приложения по умолчанию.
        - configuration_name: название конфигураций приложения.
        - db_field: название полей в БД.
        - crud_payload: управление таблицей с полезной нагрузкой.
        - crud_config: управление таблицей с конфигурацией приложения.
        - root: экземпляр класса из библиотеки tkinter - основа приложения.
        - style: отвечает за стиль приложения.
        """
        self.default_config = DefaultConfig.get_default_config()
        self.configuration_name = Config
        self.db_field = ConstantDataBase
        self.crud_payload = crud_payload
        self.crud_config = crud_config
        self.root = Tk()
        self.style = Style()

    def start(self):
        """
        Запустит цепочку команд:
        - создаст базу данных (если её нет) и таблицу в ней для полезной
          нагрузки (если её нет),
        - создаст таблицу для хранения конфигурации приложения (если её нет),
        - заполнит таблицу для хранения конфигурации приложения значениями
          по умолчанию, если она ещё не заполнена.
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
        """
        Установит переменные, которые будут отслеживаться приложением,
        для главного окна.
        """
        self.search_by_input = StringVar()
        self.password_by_output = StringVar()

    def install_everything_variable_for_create_and_update_window(self) -> None:
        """
        Установит переменные, которые будут отслеживаться приложением,
        для окна создания новой записи в БД.
        """
        self.slug_field = StringVar()
        self.password_field = StringVar()

    def install_everything_variable_for_all_note_window(self) -> None:
        """
        Установит переменные, которые будут отслеживаться приложением,
        для окна всех записей.
        """
        data_all_db = self.crud_payload.get_all_slag()

        self.list_entry = Variable(value=data_all_db)
        self.selected_one_entry = StringVar()

    def install_everything_variable_for_config_window(self) -> None:
        """
        Установит переменные, которые будут отслеживаться приложением,
        для окна конфигурации.
        """
        config_db = crud_config.get_all_settings()

        self.config_localization_app = StringVar(
            value=config_db[self.configuration_name.localization_app],
        )
        self.config_capital_letters = BooleanVar(
            value=config_db[self.configuration_name.capital_letters],
        )
        self.config_numbers = BooleanVar(
            value=config_db[self.configuration_name.numbers],
        )
        self.config_characters = BooleanVar(
            value=config_db[self.configuration_name.characters],
        )
        self.config_min_length_password = IntVar(
            value=config_db[self.configuration_name.min_length_password],
        )
        self.config_max_length_password = IntVar(
            value=config_db[self.configuration_name.max_length_password],
        )

    def open_main_window(self) -> None:
        """Откроет главное окно, описывает его логику работы."""
        self.install_everything_variable_for_main_window()

        window = self.configure_window(
            window=self.root,
            title=self.localization.title_window_main,
            iconbitmap=ICONBITMAP,
        )
        self.set_up_column_and_row_settings(
            window=window,
            number_row=3,
            number_column=4,
        )
        self.add_entry_field(
            master=window,
            textvariable=self.search_by_input,
            row=0,
            column=0,
            columnspan=3,
        )
        self.add_label(
            master=window,
            row=1,
            column=0,
            columnspan=3,
            textvariable=self.password_by_output,
            borderwidth=2,
            relief=SUNKEN,
        )
        data_button = (
            {
                'text': self.localization.button_create,
                'row': 2,
                'column': 0,
                'command': lambda: self.open_create_and_update_window(
                    window_master=window
                ),
            },
            {
                'text': self.localization.button_updata,
                'row': 2,
                'column': 1,
                'command': lambda: self.open_create_and_update_window(
                    window_master=window, update=True
                ),
            },
            {
                'text': self.localization.button_all_note,
                'row': 2,
                'column': 2,
                'command': lambda: self.open_all_notes_window(
                    window_master=window
                ),
            },
            {
                'text': self.localization.button_search,
                'row': 0,
                'column': 3,
                'command': lambda: self.search_entry_in_db(),
            },
            {
                'text': self.localization.button_copy,
                'row': 1,
                'column': 3,
                'command': lambda: self.copy_to_clipboard(window),
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

        def bind_escape(_):
            """Выполнится при нажатие ESC."""
            self.search_by_input.set('')
            self.password_by_output.set('')

        window.bind('<Escape>', bind_escape)
        window.bind('<Return>', lambda _: self.search_entry_in_db())

        window.mainloop()

    def open_create_and_update_window(
        self,
        window_master: Tk | Toplevel,
        update: bool = False
    ) -> None:
        """
        Откроет окно для создания новой записи в БД или редактирования уже
        существующей.

        - window_master: мастер окно, из которого было запущено это окно,
        - update: если True, то откроет окно для обновления существующей
          записи, иначе для создания новой.
        """
        self.install_everything_variable_for_create_and_update_window()

        self.slug_field.set(self.search_by_input.get())

        if update:
            data_db = self.crud_payload.get_by_slug_or_none(
                self.search_by_input.get()
            )
            if data_db is None:
                showerror(
                    'Нет записи',
                    'Записи с данным слагом не найдено.'
                )
                return
            title_window = 'Изменить запись'
            title_button_ok = 'Сохранить'
            self.password_field.set(data_db[self.db_field.password])
            id_to_update = data_db['id']
        else:
            title_window = 'Создать новую запись'
            title_button_ok = 'Создать'
            self.password_field.set(self.password_by_output.get())
            id_to_update = None

        window = Toplevel(window_master)
        self.configure_window(
            window=window,
            title=title_window,
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
                'text': 'Короткое название '
                        '(сохранится без пробелов по краям):',
                'row': 0,
            },
            {
                'text': 'Более подробное описание, чтоб не забыть, '
                        'про что это вообще:',
                'row': 2,
            },
            {
                'text': 'Пароль, для указанного артефакта '
                        '(сохранится без пробелов):',
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

        if update:
            text_field.set(data_db[self.db_field.description])

        def set_value_entry_password():
            """Запустит цепочку генерации пароля."""
            config_db = crud_config.get_all_settings()
            self.password_field.set(generate_password(
                min_range_pass=(
                    config_db[self.configuration_name.min_length_password]
                ),
                max_range_pass=(
                    config_db[self.configuration_name.max_length_password]
                ),
                number=int(config_db[self.configuration_name.numbers]),
                characters=int(config_db[self.configuration_name.characters]),
                capital_letters=int(
                    config_db[self.configuration_name.capital_letters]
                ),
            ))

        data_button = [
            {
                'text': 'Сгенерировать',
                'command': lambda: set_value_entry_password(),
                'column': 0,
            },
            {
                'text': title_button_ok,
                'command': lambda: self.create_or_update_entry_in_database(
                    slug=self.slug_field.get(),
                    description=text_field.get(),
                    password=self.password_field.get(),
                    window=window,
                    id_to_update=id_to_update,
                ),
                'column': 2,
            },
            {
                'text': 'Отмена',
                'command': lambda: self.dismiss(window),
                'column': 3,
            },
        ]
        if update:
            data_button.append(
                {
                    'text': 'Удалить',
                    'command': lambda: self.remove_entry_db(window),
                    'column': 1,
                },
            )
        for button in data_button:
            self.add_button(
                master=window,
                row=6,
                **button,
            )

    def open_all_notes_window(self, window_master: Tk | Toplevel) -> None:
        """Откроет окно всех записей в БД."""
        self.install_everything_variable_for_all_note_window()

        window = Toplevel(window_master)
        self.configure_window(
            window=window,
            title='Все записи',
            grab_set=True,
            focus_force=True,
        )
        self.set_up_column_and_row_settings(
            window=window,
            number_row=2,
            number_column=3,
        )
        listbox = self.add_listbox(
            master=window,
            listvariable=self.list_entry,
            row=0,
            column=0,
            columnspan=3,
            height=min(len(self.list_entry.get()), 20),
            command=lambda _: self.selected_one_entry.set(
                listbox.get(
                    listbox.curselection()[0]
                )[0]
            ),
        )

        data_button = (
            {
                'text': 'Выбрать',
                'column': 0,
                'command': lambda: self.select_from_all_notes(window),
            },
            {
                'text': 'Отменить',
                'column': 2,
                'command': lambda: self.dismiss(window),
            },
        )
        for button in data_button:
            self.add_button(
                master=window,
                row=1,
                **button,
            )

        window.bind('<Return>', lambda _: self.select_from_all_notes(window))
        window.bind(
            '<Double-Button-1>', lambda _: self.select_from_all_notes(window)
        )

    def open_config_window(self, window_master: Tk | Toplevel) -> None:
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
                spinbox_max_length_password.config(
                    from_=int(spinbox_min_length_password.get())
                )
                spinbox_min_length_password.config(
                    to=int(spinbox_max_length_password.get())
                )
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

        window.bind('<Return>', lambda _: self.save_config(window))

    def open_about_window(self, window_master: Tk | Toplevel) -> None:
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

    def copy_to_clipboard(self, window: Tk | Toplevel) -> None:
        """Скопирует пароль в буфер обмена."""
        window.clipboard_clear()
        window.clipboard_append(self.password_by_output.get())
        window.update()

    def create_or_update_entry_in_database(
        self,
        slug: str,
        password: str,
        description: str,
        window: Tk | Toplevel,
        id_to_update: str | None = None,
    ) -> None:
        """
        Создаст новую запись в базе данных или обновит новую по переданному id.
        Проведет валидацию форм.
        В конце закроет окно для создания записи в БД.

        - slug: значение для поля slug,
        - password: значение для поля password,
        - description: значение для поля description,
        - window: окно, которое необходимо закрыть по завершению,
        - id_to_update: если None - то создаст новую запись, если передан id,
          то изменит запись по этому id.
        """
        data_db = self.crud_payload.get_by_slug_or_none(slug=slug)
        if not slug:
            showerror(
                title='Исправьте ввод',
                message='Короткое название не может быть пустым',
            )
        elif self.crud_payload.get_by_slug_or_none(slug=slug) and (
            id_to_update is None or id_to_update != data_db['id']
        ):
            showerror(
                title='Исправьте ввод',
                message='Такое короткое название уже есть в базе данных',
            )
        elif not password:
            showerror(
                title='Исправьте ввод',
                message='Пароль не может быть пустым',
            )
        else:
            slug_corrected = slug.strip()
            password_corrected = password.strip().replace(' ', '')
            if id_to_update:
                self.crud_payload.update_entry(
                    id=id_to_update,
                    slug=slug_corrected,
                    description=description,
                    password=password_corrected,
                )
            else:
                self.crud_payload.create_entry(
                    slug=slug_corrected,
                    description=description,
                    password=password_corrected,
                )
            self.search_by_input.set(slug_corrected)
            self.password_by_output.set(password_corrected)
            self.dismiss(window)

    def remove_entry_db(self, window: Tk | Toplevel) -> None:
        """Удалит данную запись из базы данных."""
        remove_entry_slug = self.search_by_input.get()
        result = askyesno(
            title='Удаление',
            message=(
                f'Вы точно хотите удалить запись "{remove_entry_slug}" '
                'из базы данных?\n'
                'Восстановить будет невозможно!'
            ),
        )
        if result:
            self.crud_payload.delete_by_slug(remove_entry_slug)
            self.search_by_input.set('')
            self.password_by_output.set('')
            self.dismiss(window)

    def select_from_all_notes(self, window: Tk | Toplevel) -> None:
        """Обрабатывает работу кнопки "Выбрать" окна со всеми записями."""
        note_db = self.crud_payload.get_by_slug_or_none(
            self.selected_one_entry.get()
        )
        if note_db is not None:
            self.search_by_input.set(note_db[self.db_field.slug])
            self.password_by_output.set(note_db[self.db_field.password])
            self.dismiss(window)

    def search_entry_in_db(self) -> None:
        """
        Найдет пароль в базе данных по слагу и выведет его на главном окне.
        """
        data_db = self.crud_payload.get_by_slug_or_none(
            self.search_by_input.get()
        )
        self.password_by_output.set(
            'Ничего не найдено'
            if data_db is None
            else data_db[self.db_field.password]
        )

    def save_config(self, window: Tk | Toplevel) -> None:
        """
        Обрабатывает работу кнопки "Принять" окна конфигурации.

        - Проверит валидность данных.
        - Сохранит изменения настроек в БД,
        - Закроет окно конфигурации.
        """
        self.validation_config()
        self.crud_config.update_all(
            {
                self.configuration_name.localization_app: (
                    self.config_localization_app.get()
                ),
                self.configuration_name.capital_letters: (
                    self.config_capital_letters.get()),
                self.configuration_name.numbers: (
                    self.config_numbers.get()
                ),
                self.configuration_name.characters: (
                    self.config_characters.get()
                ),
                self.configuration_name.min_length_password: (
                    self.config_min_length_password.get()
                ),
                self.configuration_name.max_length_password: (
                    self.config_max_length_password.get()
                ),
            }
        )
        self.dismiss(window)

    def validation_config(self) -> None:
        """
        Валидатор конфигурации.

        Если, по какой-либо причине, данные конфигурации для записи в БД будут
        не валидны, принудительно сделает их валидными, например, поставит
        значения по умолчанию.
        """
        if self.config_localization_app.get() not in [
            tag for tag, _ in LOCALIZATION_OPTIONS
        ]:
            self.config_localization_app.set(
                self.default_config[self.configuration_name.localization_app]
            )
        for value, field in (
            (
                self.config_capital_letters,
                self.configuration_name.capital_letters,
            ),
            (
                self.config_numbers,
                self.configuration_name.numbers,
            ),
            (
                self.config_characters,
                self.configuration_name.characters,
            ),
        ):
            if not isinstance(value.get(), bool):
                value.set(self.default_config[field])
        if self.config_min_length_password.get() > (
            max_ := self.config_max_length_password.get()
        ):
            self.config_min_length_password.set(max_)
