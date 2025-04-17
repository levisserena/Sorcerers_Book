from tkinter import Radiobutton, Tk, Toplevel, Variable
from tkinter.constants import W
from tkinter.ttk import Frame
from typing import Any

from app.constants.constants import FONT_REGULAR
from app.constants.length import Length


class RadiobuttonMixin:
    """Миксин для обработки работы радиокнопки."""

    def add_radiobutton(
        self,
        master: Frame | Tk | Toplevel | None,
        text: str,
        value: Any,
        variable: Variable,
        row: int,
        column: int,
        padx: int = Length.gap,
        pady: int = Length.gap,
        rowspan: int = 1,
        columnspan: int = 1,
        sticky: str = W,
    ) -> Radiobutton:
        """
        Добавит в переданный контейнер радиокнопку.

        Параметры:
        - master: к какому контейнеру будет прикреплен виджет,
        - text: текст рядом с кнопке,
        - value: значение, соответствующее кнопке,
        - variable: переменная, привязанная к кнопке,
        - row: номер строки, отсчет начинается с нуля,
        - column: номер столбца, отсчет начинается с нуля,
        - padx: отступы по горизонтали соответственно от границ ячейки грида
          до границ элемента,
        - pady: отступы по вертикали соответственно от границ ячейки грида
          до границ элемента,
        - rowspan: сколько строк должен занимать элемент,
        - columnspan: сколько столбцов должен занимать элемент,
        - sticky: выравнивание элемента в ячейке, если ячейка больше элемента.
        """
        radiobutton = Radiobutton(
            master=master,
            text=text,
            value=value,
            variable=variable,
            font=FONT_REGULAR,
        )
        radiobutton.grid(
            row=row,
            column=column,
            padx=padx,
            pady=pady,
            rowspan=rowspan,
            columnspan=columnspan,
            sticky=sticky,
        )
        return radiobutton
