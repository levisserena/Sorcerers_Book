from app.app import SorcerersBook


def main() -> None:
    """Функция, запускающая всё приложение."""
    sorcerers_book = SorcerersBook()
    sorcerers_book.start()


if __name__ == '__main__':
    main()
