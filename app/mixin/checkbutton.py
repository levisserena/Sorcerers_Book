from tkinter import Tk, Toplevel, Variable, W
from tkinter.ttk import Checkbutton

from app.constants.length import Length


class CheckbuttonMixin:
    """Миксин для обработки работы чек-кнопок."""

    def add_checkbutton(
        self,
        master: Tk | Toplevel | None,
        text: str,
        variable: Variable,
        row: int,
        column: int,
        padx: int = Length.gap,
        pady: int = Length.gap,
        rowspan: int = 1,
        columnspan: int = 1,
        sticky: str = W,
    ) -> Checkbutton:
        """
        Добавит в переданный контейнер чек-кнопку.

        Параметры:
        - master: к какому контейнеру будет прикреплен виджет,
        - text: текст на кнопке,
        - variable: привязанный к значению объект Variable,
        - row: номер строки, отсчет начинается с нуля,
        - column: номер столбца, отсчет начинается с нуля,
        - padx: отступы по горизонтали соответственно от границ ячейки грида до границ элемента,
        - pady: отступы по вертикали соответственно от границ ячейки грида до границ элемента,
        - rowspan: сколько строк должен занимать элемент,
        - columnspan: сколько столбцов должен занимать элемент,
        - sticky: выравнивание элемента в ячейке, если ячейка больше элемента.
        """
        button = Checkbutton(
            master=master,
            text=text,
            variable=variable,
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
