from tkinter import Misc, NSEW
from tkinter.ttk import Button
from typing import Any, Callable

from app.constants.length import Length


class ButtonMixin:
    """Миксин для обработки работы кнопок."""

    def add_button(
        self,
        master: Misc | None,
        text: str,
        command: str | Callable[[], Any],
        row: int,
        column: int,
        padx: int = Length.gap,
        pady: int = Length.gap,
        rowspan: int = 1,
        columnspan: int = 1,
        sticky: str = NSEW,
    ) -> Button:
        """
        Добавит в переданный контейнер кнопку.

        Параметры:
        - master: к какому контейнеру будет прикреплен виджет,
        - text: текст на кнопке,
        - command: активируемая кнопкой команда,
        - row: номер строки, отсчет начинается с нуля,
        - column: номер столбца, отсчет начинается с нуля,
        - padx: отступы по горизонтали соответственно от границ ячейки грида до границ элемента,
        - pady: отступы по вертикали соответственно от границ ячейки грида до границ элемента,
        - rowspan: сколько строк должен занимать элемент,
        - columnspan: сколько столбцов должен занимать элемент,
        - sticky: выравнивание элемента в ячейке, если ячейка больше элемента.
        """
        button = Button(
            master=master,
            text=text,
            command=command,
        )
        button.grid(
            row=row,
            column=column,
            padx=padx,
            pady=pady,
            rowspan=rowspan,
            columnspan=columnspan,
            sticky=sticky,
        )
        return button
