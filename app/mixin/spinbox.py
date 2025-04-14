from tkinter import Misc, W, Variable
from tkinter.ttk import Spinbox

from app.constants.constants import FONT_REGULAR
from app.constants.length import Length


class SpinboxMixin():
    """Миксин для обработки работы спинбокса."""

    def add_spinbox(
        self,
        master: Misc | None,
        textvariable: Variable,
        from_: int,
        to: int,
        row: int,
        column: int,
        command=None,
        increment: int = 1,
        width: int = 5,
        state='readonly',
        padx: int = Length.gap,
        pady: int = Length.gap,
        rowspan: int = 1,
        columnspan: int = 1,
        sticky: str = W,
    ) -> Spinbox:
        """
        Добавит в переданный контейнер спинбокс.

        Параметры:
        - master: к какому контейнеру будет прикреплен виджет,
        - textvariable: устанавливает привязку к элементу Variable,
        - row: номер строки, отсчет начинается с нуля,
        - column: номер столбца, отсчет начинается с нуля,
        - padx: отступы по горизонтали соответственно от границ ячейки грида до границ элемента,
        - pady: отступы по вертикали соответственно от границ ячейки грида до границ элемента,
        - rowspan: сколько строк должен занимать элемент,
        - columnspan: сколько столбцов должен занимать элемент,
        - sticky: выравнивание элемента в ячейке, если ячейка больше элемента.
        """
        spinbox = Spinbox(
            master=master,
            from_=from_,
            to=to,
            increment=increment,
            width=width,
            textvariable=textvariable,
            state=state,
            command=command,
            font=FONT_REGULAR,
        )
        spinbox.grid(
            row=row,
            column=column,
            padx=padx,
            pady=pady,
            rowspan=rowspan,
            columnspan=columnspan,
            sticky=sticky,
        )
        return spinbox
