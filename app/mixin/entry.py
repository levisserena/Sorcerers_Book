from tkinter import Tk, Toplevel, Variable
from tkinter.constants import NSEW
from tkinter.ttk import Entry, Frame

from app.constants.constants import FONT_REGULAR
from app.constants.length import Length


class EntryMixin():
    """Миксин для обработки работы полей ввода."""

    def add_entry_field(
        self,
        master: Frame | Tk | Toplevel | None,
        textvariable: Variable,
        row: int,
        column: int,
        padx: int = Length.gap,
        pady: int = Length.gap,
        rowspan: int = 1,
        columnspan: int = 1,
        sticky: str = NSEW,
    ) -> Entry:
        """
        Добавит в переданный контейнер поле для ввода.

        Параметры:
        - master: к какому контейнеру будет прикреплен виджет,
        - textvariable: устанавливает привязку к элементу Variable,
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
        entry = Entry(
            master=master,
            textvariable=textvariable,
            font=FONT_REGULAR,
        )
        entry.grid(
            row=row,
            column=column,
            padx=padx,
            pady=pady,
            rowspan=rowspan,
            columnspan=columnspan,
            sticky=sticky,
        )
        return entry
