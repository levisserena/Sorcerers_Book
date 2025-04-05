from tkinter import Tk, Toplevel

from app.constants.length import Length


class WindowMixin:
    """Миксин для обработки работы окон."""

    def configure_window(
        self,
        window: Tk | Toplevel,
        title: str,
        geometry: str | None = None,
        iconbitmap: str | None = None,
        grab_set: bool = False,
        focus_force: bool = False,
        resizable: bool = False,
    ) -> Tk | Toplevel:
        """
        Откроет окно с указанными параметрами.

        Параметры:
        window: основа для окна, например Tk или Toplevel,
        title: название окна,
        geometry: размеры окна,
        iconbitmap: иконка окна,
        grab_set: перехватывает ли окно управление при создании,
        focus_force: сразу ли активно окно при открытие,
        resizable: можно ли менять размеры окна.

        Вернет экземпляр этого окна.
        """
        window.title(title)
        if geometry is not None:
            window.geometry(geometry)
        if iconbitmap is not None:
            window.iconbitmap(default=iconbitmap)
        window.resizable(resizable, resizable)
        if focus_force:
            window.focus_force()
        if grab_set:
            window.grab_set()
            window.protocol(
                'WM_DELETE_WINDOW',  # перехватываем нажатие на крестик
                lambda: self.dismiss(window),
            )
        return window

    def dismiss(self, window: Tk | Toplevel):
        """
        Принимает окно, возвращает контроль другому окну,
        закрывает переданное окно.
        """
        window.grab_release()
        window.destroy()

    def set_up_column_and_row_settings(
        self,
        window: Tk | Toplevel,
        number_row: int = 1,
        number_column: int = 1,
        minsize_row: int = Length.widget_height,
        minsize_column: int = Length.widget_width,
        weight: int = 0,
    ) -> None:
        for index in range(number_row):
            window.rowconfigure(index=index, minsize=minsize_row, weight=weight)
        for index in range(number_column):
            window.columnconfigure(index=index, minsize=minsize_column, weight=weight)
