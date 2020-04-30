from tkinter import ttk 
from constants import *

def init_styles():

    white = "#FFFFFF"
    red = "#D09696"

    # Main style settings
    theme_style = ttk.Style()
    theme_style_list = ['TFrame', 'TLabel', 'TLabelframe', 'TLabelframe.Label', 'TButton', 'TNotebook', 'TNotebook.Tab', 'TCheckbutton', 'TPanedwindow']
    
    ## Background setup
    for i in range(len(theme_style_list)):
        theme_style.configure(theme_style_list[i],background=white)

    ## Frame setup
    # theme_style.configure('TFrame', paddind=)

    ## Notebook tab setup
    theme_style.configure('TNotebook.Tab', padding=[25,5], background=red)
    # expand: enlarge the tab size when selected
    theme_style.map('TNotebook.Tab', background=[("selected", white)], expand=[("selected", [1,1,1,0])])

    red_style = ttk.Style()
    red_style_name = 'red'
    red_style_list = ['TFrame','TNotebook', 'TButton']
    for i in range(len(red_style_list)):
        red_style_list[i] = red_style_name+'.'+red_style_list[i]
        red_style.configure(red_style_list[i], background=red)
    ## Notebook setup
    red_style.configure('red.TNotebook', tabmargins=[1, 0, 1, 0])
    

