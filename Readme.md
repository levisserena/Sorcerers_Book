# Sorcerers Book

- [О проекте](#about)
- [Планы на реализацию](#plans)
- [Локализация проекта](#localization)
- [Компиляция](#compilation)
- [Полезные статьи](#bonus)

## О проекте <a name="about"></a> 

**Sorcerers Book** — или **Книжка Колдуна**, это небольшое приложение для хранения пометок, в частности: паролей от всего и вся.
Не подразумевает под собой какой-либо защищенный кейс. Только для сбора всего в одном месте. Чтобы не забывать.
Поддерживает генерацию паролей, чтоб не выдумывать.

## Планы на реализацию <a name="plans"></a> 

- Возможность в настройках менять масштаб приложения.
- Хранение паролей в БД в зашифрованном виде. Продумать стратегию шифрования и дешифрования.
- Локализовать приложение на английский язык.
- Предусмотреть логирование в txt файл. Нужно для скомпилированного приложения.
- Подготовить документацию (Этот Readme.md)

## Локализация проекта <a name="localization"></a> 
### TODO сделать норм пути
xgettext -d loc -o loc.pot localization/localization.py --from-code=UTF-8 - команда для создания pot файла

в pot пишем перевод

### TODO сделать норм пути
msgfmt loc.pot -o locales/loc.mo  - для компиляции в mo файл


## Компиляция <a name="compilation"></a> 
Устанавливаем Nuitka в активированном виртуальном окружении.
```
pip install nuitka
```
Проверяем установку
```
python -m nuitka --version
```
Запускаем компиляцию
```
python -m nuitka --onefile --windows-disable-console --output-dir=sorcerers-book --output-filename=book.exe --windows-icon-from-ico=static/sb.ico --enable-plugin=tk-inter main.py
```
| Флаг                                  | Описание                                                               |
|---------------------------------------|------------------------------------------------------------------------|
| --onefile                             | Создать один .exe (уменьшит количество зависимостей).                  |
| --windows-disable-console             | Скрыть консоль при запуске GUI-приложений на Tkinter.                  |
| --output-dir=sorcerers-book           | Создаст папку sorcerers-book, куда сложит все файлы                    |
| --output-filename=book.exe            | Задать имя выходного файла <br>(book.exe вместо стандартного main.exe).|
| --enable-plugin=tk-inter              | Нужно для корректной работы Tkinter.                                   |
| --windows-icon-from-ico=static/sb.ico | Установит иконку для файла .exe.                                       |

На все вопросы соглашайтесь - будет скачен компилятор C++ и необходимые файлы.

После завершения компиляции в папку `dist` нужно будет скопировать папку `static` вместе со всем содержимым.

## Полезные статьи <a name="bonus"></a> 
Про встроенную библиотеку [sqlite3](https://habr.com/ru/articles/754400/).<br>
Про встроенную библиотеку [tkinter](https://metanit.com/python/tkinter/1.1.php).