from tkinter import END, Misc, NSEW, WORD
from tkinter.scrolledtext import ScrolledText
from typing import Literal, Protocol

from app.constants.constants import FONT_REGULAR
from app.constants.length import Length


class TextFieldP(Protocol):
    """Протокол класса обертки для текстового виджета."""

    def __init__(self, text_widget):
        """text_widget: текстовый виджет."""
        self.text_widget = text_widget

    def get(self):
        """Вернет значение текстового виджета."""
        raise NotImplementedError

    def set(self, value):
        """Заменит значение текстового виджета."""
        raise NotImplementedError


class TextMixin():
    """Миксин для обработки работы полей ввода."""

    def add_text_field(
        self,
        master: Misc | None,
        row: int,
        column: int,
        wrap: Literal['word', 'char', 'none'] = WORD,
        width: int = 50,
        height: int = 10,
        padx: int = Length.gap,
        pady: int = Length.gap,
        rowspan: int = 1,
        columnspan: int = 1,
        sticky: str = NSEW,
    ) -> TextFieldP:
        """
        Добавит в переданный контейнер поле для многострочного ввода.

        Параметры:
        - master: к какому контейнеру будет прикреплен виджет,
        - row: номер строки, отсчет начинается с нуля,
        - column: номер столбца, отсчет начинается с нуля,
        - wrap: переносы,
        - width: ширина поля для ввода в символах,
        - height: высота поля для ввода в строках,
        - padx: отступы по горизонтали соответственно от границ ячейки грида до границ элемента,
        - pady: отступы по вертикали соответственно от границ ячейки грида до границ элемента,
        - rowspan: сколько строк должен занимать элемент,
        - columnspan: сколько столбцов должен занимать элемент,
        - sticky: выравнивание элемента в ячейке, если ячейка больше элемента.
        """

        class TextField:
            """Класс обертка для текстового поля."""

            def __init__(self, text_widget):
                """text_widget: текстовый виджет."""
                self.text_widget = text_widget

            def get(self):
                """Вернет значение текстового виджета."""
                return self.text_widget.get('1.0', 'end-1c')

            def set(self, value):
                """Заменит значение текстового виджета."""
                self.text_widget.delete('1.0', END)
                self.text_widget.insert(END, value)

        text = ScrolledText(
            master=master,
            wrap=wrap,
            width=width,
            height=height,
            font=FONT_REGULAR,
        )
        text.grid(
            row=row,
            column=column,
            padx=padx,
            pady=pady,
            rowspan=rowspan,
            columnspan=columnspan,
            sticky=sticky,
        )
        return TextField(text)
