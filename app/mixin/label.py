from tkinter import Misc, NSEW, Variable
from tkinter.ttk import Label
from tkinter.constants import SUNKEN

from app.constants.length import Length


class LabelMixin:
    """Миксин для отображения строкового вывода."""

    def add_label(
        self,
        master: Misc | None,
        row: int,
        column: int,
        text: float | str = '',
        textvariable: Variable | None = None,
        padx: int = Length.gap,
        pady: int = Length.gap,
        rowspan: int = 1,
        columnspan: int = 1,
        borderwidth: int = 2,
        relief=SUNKEN,  # TODO: лучше б убрать SUNKEN и поставить нейтральное.
        sticky: str = NSEW,
    ) -> Label:
        """
        Добавит в переданный контейнер поле для вывода.

        Параметры:
        master: к какому контейнеру будет прикреплен виджет,
        text: выводимый текст,
        textvariable: устанавливает привязку к элементу Variable,
        row: номер строки, отсчет начинается с нуля,
        column: номер столбца, отсчет начинается с нуля,
        padx: отступы по горизонтали соответственно от границ ячейки грида до границ элемента,
        pady: отступы по вертикали соответственно от границ ячейки грида до границ элемента,
        rowspan: сколько строк должен занимать элемент,
        columnspan: сколько столбцов должен занимать элемент,
        borderwidth: ширина линии контура,
        relief: рельеф полотна поля,
        sticky: выравнивание элемента в ячейке, если ячейка больше элемента.
        """
        label = Label(
            master=master,
            text=text,
            textvariable=textvariable,
            borderwidth=borderwidth,
            relief=relief,
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
