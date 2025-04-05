from dataclasses import dataclass


@dataclass
class ConstantDataBase:
    """
    Константы для создания БД и таблиц в ней.

    Названия БД и таблиц в ней:
    name_db: имя файла БД.
    name_table_payload: название таблицы с полезной нагрузкой.
    name_table_config: название таблицы с настройками.

    Поля:
    slug: поле слаг, по которому будет поиск.
    description: описание.
    password: пароль, который хотим сохранить.
    name: название настройки.
    value: значение настройки.
    """

    name_db: str = 'grimoire.db'

    name_table_payload: str = 'scroll'
    name_table_config: str = 'config'

    slug: str = 'slug'
    description: str = 'description'
    password: str = 'password'
    name: str = 'name'
    value: str = 'value'
