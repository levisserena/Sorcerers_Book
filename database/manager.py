from sqlite3 import connect


class Connector:
    """Контекстный менеджер подключения к базе данных."""

    def __init__(self, name_db: str):
        """
        Контекстный менеджер подключения к базе данных.

        Параметры:
            name_db имя файла с БД.
        """
        self.name_db: str = name_db

    def __enter__(self):
        self.connection = connect(self.name_db)
        return self.connection.cursor()

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            self.connection.commit()
        finally:
            self.connection.close()
