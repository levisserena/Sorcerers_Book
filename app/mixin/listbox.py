from tkinter import Event, Listbox, Tk, Toplevel, Variable
from tkinter.constants import BROWSE, NSEW, NONE
from tkinter.ttk import Frame
from typing import Callable, Literal

from app.constants.constants import FONT_REGULAR
from app.constants.length import Length


class ListboxMixin():
    """Миксин для обработки работы листбокс."""

    def add_listbox(
        self,
        master: Frame | Tk | Toplevel | None,
        listvariable: Variable,
        row: int,
        column: int,
        command: Callable[[Event], object] | None,
        padx: int = Length.gap,
        pady: int = Length.gap,
        rowspan: int = 1,
        columnspan: int = 1,
        sticky: str = NSEW,
        selectmode: Literal[
            'single', 'browse', 'multiple', 'extended'
        ] = BROWSE,
        height: int = 10,
        width: int = 20,
    ) -> Listbox:
        """
        Добавит в переданный контейнер листбокс.

        Параметры:
        - master: к какому контейнеру будет прикреплен виджет,
        - listvariable: устанавливает привязку к элементу Variable,
        - row: номер строки, отсчет начинается с нуля,
        - column: номер столбца, отсчет начинается с нуля,
        - command: команда, выполняемая при изменение выбора элемента в
          листбоксе,
        - padx: отступы по горизонтали соответственно от границ ячейки грида
          до границ элемента,
        - pady: отступы по вертикали соответственно от границ ячейки грида
          до границ элемента,
        - rowspan: сколько строк должен занимать элемент,
        - columnspan: сколько столбцов должен занимать элемент,
        - sticky: выравнивание элемента в ячейке, если ячейка больше элемента,
        - selectmode: поддержка нескольких выборов,
        - height: высота виджета в строках,
        - width: ширина виджета в символах.
        """
        listbox = Listbox(
            master=master,
            listvariable=listvariable,
            selectmode=selectmode,
            height=height,
            width=width,
            font=FONT_REGULAR,
            activestyle=NONE,
        )
        listbox.grid(
            row=row,
            column=column,
            padx=padx,
            pady=pady,
            rowspan=rowspan,
            columnspan=columnspan,
            sticky=sticky,
        )
        listbox.bind("<<ListboxSelect>>", command)
        return listbox
