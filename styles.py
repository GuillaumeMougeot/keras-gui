from tkinter import ttk 
from constants import *

def init_styles():
    style = ttk.Style()

    white = "#FFFFFF"
    red = "#D09696"

    style.theme_create( "keras_gui", parent=style.theme_use(), settings={
        "TFrame":
        {
            "configure":    {"background": white}
        },
        "TLabelframe":
        {
            "configure":    {"background": white}
        },
        "TLabelframe.Label":
        {
            "configure":    {"background": white}
        },
        "TNotebook": 
        {
            "configure":    {"tabmargins": [2, 5, 2, 0] } 
        },
        "TNotebook.Tab": 
        {
            "configure":    {"padding": [5, 1], "background": white },
            "map":          {"background": [("selected", white)],
                            "expand": [("selected", [1, 1, 1, 0])] } 
        },
        "TButton":
        {
            "configure":    {"background": white}
        },
        "TLabel":
        {
            "configure":    {"background": white}
        }
    })

    style.theme_use("keras_gui")

    # white_style = ttk.Style()
    # white_style.configure(FRAME_STYLE, background='white')
    # white_style.configure(LABELFRAME_STYLE, background='white')
    # white_style.configure(LABELFRAME_LABEL_STYLE, background='white')
    # white_style.configure(BUTTON_STYLE, background='white')

    red_style = ttk.Style()
    red_style.configure(ROOT_FRAME_STYLE, background='#D09696')
    # red_style.configure(NOTEBOOK_STYLE, background='#D09696')
    # red_style.configure(NOTEBOOK_TAB_STYLE, background='#D09696')
