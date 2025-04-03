from database.constant import DefaultSetting
from database.crud import crud_payload, crud_setting


def create_all_db() -> None:
    """
    Создаст файл базы данных если его нет,
    и создаст таблицы в нем, если их нет.
    """
    crud_payload.create_db()
    crud_setting.create_db()


def default_settings(setting: type[DefaultSetting]) -> None:
    """Заполнит таблицу Setting в базе данных, тем самым, установит первоначальные настройки."""
    all_default_settings = {
        setting.localization: setting.default_localization,
        setting.capital_letters: setting.true,
        setting.numbers: setting.true,
        setting.characters: setting.true,
        setting.min_length_password: setting.default_length_password,
        setting.max_length_password: setting.default_length_password,
    }
    crud_setting.create_rows_in_db(all_default_settings)
