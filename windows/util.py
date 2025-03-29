def dismiss(window):
    """
    Принимает окно, возвращает контроль другому окну,
    закрывает переданное окно.
    """
    window.grab_release()
    window.destroy()
