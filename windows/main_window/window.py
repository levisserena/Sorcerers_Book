from tkinter.constants import SUNKEN
from tkinter.ttk import Button, Entry, Label

from windows.constants import Length as lng
from windows.setting_window.setting_window import open_setting_window


def window(root, localization):

    root.title(localization.title)
    root.geometry('{}x{}'.format(
        lng.gap*3+lng.entry_width+lng.widget_width,
        lng.gap*4+lng.widget_height*3,
    ))
    root.iconbitmap(default='static/sb.ico')
    root.resizable(False, False)

    entry = Entry()
    entry.place(
        x=lng.gap,
        y=lng.gap,
        height=lng.widget_height,
        width=lng.entry_width,
    )

    label = Label(
        text='ULzt6uEF68WQ4GEgdKP61WohnEc2N7mJ4TLpnVy9',
        borderwidth=2,
        relief=SUNKEN,
    )
    label.place(
        x=lng.gap,
        y=lng.gap*2+lng.widget_height,
        height=lng.widget_height,
        width=lng.entry_width,
    )

    button_search = Button(text=localization.button_search)
    button_search.place(
        x=lng.gap*2+lng.entry_width,
        y=lng.gap,
        height=lng.widget_height,
        width=lng.widget_width,
    )

    button_copy = Button(text=localization.button_copy)
    button_copy.place(
        x=lng.gap*2+lng.entry_width,
        y=lng.gap*2+lng.widget_height,
        height=lng.widget_height,
        width=lng.widget_width,
    )

    button_create = Button(text=localization.button_create)
    button_create.place(
        x=lng.gap,
        y=lng.gap*3+lng.widget_height*2,
        height=lng.widget_height,
        width=lng.widget_width,
    )

    button_updata = Button(text=localization.button_updata)
    button_updata.place(
        x=lng.gap*2+lng.widget_width,
        y=lng.gap*3+lng.widget_height*2,
        height=lng.widget_height,
        width=lng.widget_width,
    )

    button_all_note = Button(text=localization.button_all_note)
    button_all_note.place(
        x=lng.gap*3+lng.widget_width*2,
        y=lng.gap*3+lng.widget_height*2,
        height=lng.widget_height,
        width=lng.widget_width,
    )

    button_setting = Button(
        text=localization.button_setting,
        command=lambda: open_setting_window(localization),
    )
    button_setting.place(
        x=lng.gap*2+lng.entry_width,
        y=lng.gap*3+lng.widget_height*2,
        height=lng.widget_height,
        width=lng.widget_width,
    )

    root.mainloop()
