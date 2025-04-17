import webbrowser
from tkinter import Tk, Toplevel, Variable
from tkinter.constants import FLAT, LEFT, NSEW
from tkinter.ttk import Frame, Label
from typing import Literal

from app.constants.constants import FONT_REGULAR, FONT_UNDERLINED
from app.constants.length import Length


class LabelMixin:
    """Миксин для обработки работы поле для вывода."""

    def add_label(
        self,
        master: Frame | Tk | Toplevel | None,
        row: int,
        column: int,
        text: float | str = '',
        textvariable: Variable | None = None,
        padx: int = Length.gap,
        pady: int = Length.gap,
        rowspan: int = 1,
        columnspan: int = 1,
        borderwidth: int = 0,
        relief: Literal[
            'raised', 'sunken', 'flat', 'ridge', 'solid', 'groove'
        ] = FLAT,
        sticky: str = NSEW,
        justify: Literal['left', 'center', 'right'] = LEFT,
    ) -> Label:
        """
        Добавит в переданный контейнер поле для вывода.

        Параметры:
        - master: к какому контейнеру будет прикреплен виджет,
        - text: выводимый текст,
        - textvariable: устанавливает привязку к элементу Variable,
        - row: номер строки, отсчет начинается с нуля,
        - column: номер столбца, отсчет начинается с нуля,
        - padx: отступы по горизонтали соответственно от границ ячейки грида
          до границ элемента,
        - pady: отступы по вертикали соответственно от границ ячейки грида
          до границ элемента,
        - rowspan: сколько строк должен занимать элемент,
        - columnspan: сколько столбцов должен занимать элемент,
        - borderwidth: ширина линии контура,
        - relief: рельеф полотна поля,
        - sticky: выравнивание элемента в ячейке, если ячейка больше элемента,
        - justify: выравнивание текста.
        """
        label = Label(
            master=master,
            text=text,
            textvariable=textvariable,
            borderwidth=borderwidth,
            relief=relief,
            justify=justify,
        )
        label.grid(
            row=row,
            column=column,
            padx=padx,
            pady=pady,
            rowspan=rowspan,
            columnspan=columnspan,
            sticky=sticky,
        )
        return label

    def add_link(
        self,
        master: Frame | Tk | Toplevel | None,
        row: int,
        column: int,
        text: float | str = '',
        textvariable: Variable | None = None,
        padx: int = Length.gap,
        pady: int = Length.gap,
        rowspan: int = 1,
        columnspan: int = 1,
        borderwidth: int = 0,
        relief: Literal[
            'raised', 'sunken', 'flat', 'ridge', 'solid', 'groove'
        ] = FLAT,
        sticky: str = NSEW,
        justify: Literal['left', 'center', 'right'] = LEFT,
    ) -> Label:
        """
        Добавит в переданный контейнер поле для вывода, с гиперссылкой.

        Параметры:
        - master: к какому контейнеру будет прикреплен виджет,
        - text: выводимый текст,
        - textvariable: устанавливает привязку к элементу Variable,
        - row: номер строки, отсчет начинается с нуля,
        - column: номер столбца, отсчет начинается с нуля,
        - padx: отступы по горизонтали соответственно от границ ячейки грида
          до границ элемента,
        - pady: отступы по вертикали соответственно от границ ячейки грида
          до границ элемента,
        - rowspan: сколько строк должен занимать элемент,
        - columnspan: сколько столбцов должен занимать элемент,
        - borderwidth: ширина линии контура,
        - relief: рельеф полотна поля,
        - sticky: выравнивание элемента в ячейке, если ячейка больше элемента,
        - justify: выравнивание текста.
        """
        link = self.add_label(
            master=master,
            row=row,
            column=column,
            text=text,
            textvariable=textvariable,
            padx=padx,
            pady=pady,
            rowspan=rowspan,
            columnspan=columnspan,
            borderwidth=borderwidth,
            relief=relief,
            sticky=sticky,
            justify=justify,
        )
        link.config(foreground="blue",)

        def on_enter(*args, **kwargs):
            """Подчеркнет ссылку."""
            link.config(font=FONT_UNDERLINED)

        def on_leave(*args, **kwargs):
            """Ссылка будет без подчеркивания."""
            link.config(font=FONT_REGULAR)

        def open_link():
            """Перейдет по ссылке."""
            if text.startswith('https://'):
                webbrowser.open(text)

        link.bind('<Button-1>', lambda e: open_link())
        link.bind('<Enter>', on_enter)
        link.bind('<Leave>', on_leave)

        return link
