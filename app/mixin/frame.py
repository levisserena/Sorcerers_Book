from tkinter import Misc, NSEW
from tkinter.ttk import Frame
from tkinter.constants import GROOVE
from typing import Literal

from app.constants.length import Length


class FrameMixin:
    """Миксин для обработки работы фреймов."""

    def add_frame(
        self,
        master: Misc | None,
        row: int,
        column: int,
        padding: int = 0,
        padx: int = Length.gap,
        pady: int = Length.gap,
        rowspan: int = 1,
        columnspan: int = 1,
        borderwidth: int = 0,
        relief: Literal['raised', 'sunken', 'flat', 'ridge', 'solid', 'groove'] = GROOVE,
        sticky: str = NSEW,
    ) -> Frame:
        """
        Добавит в переданный контейнер фрейм.

        Параметры:
        - master: к какому контейнеру будет прикреплен виджет,
        - text: выводимый текст,
        - textvariable: устанавливает привязку к элементу Variable,
        - row: номер строки, отсчет начинается с нуля,
        - column: номер столбца, отсчет начинается с нуля,
        - padx: отступы по горизонтали соответственно от границ ячейки грида до границ элемента,
        - pady: отступы по вертикали соответственно от границ ячейки грида до границ элемента,
        - rowspan: сколько строк должен занимать элемент,
        - columnspan: сколько столбцов должен занимать элемент,
        - borderwidth: ширина линии контура,
        - relief: рельеф полотна поля,
        - sticky: выравнивание элемента в ячейке, если ячейка больше элемента.
        """
        label = Frame(
            master=master,
            borderwidth=borderwidth,
            relief=relief,
            padding=padding,
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
