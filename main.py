from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from styles import init_styles
from DataTab import DataTab
from ModelTab import ModelTab
from TrainTab import TrainTab
from TestTab import TestTab
from constants import *

class Root(Tk):
    def __init__(self):
        # Stage 0 (root)
        super(Root, self).__init__()
        self.title("Keras GUI")
        self.geometry("720x720")
        self.minsize(360,360)
        self.iconbitmap("icons/logo.ico")
        self.config(background='#D00000')

        # Initiate styles
        init_styles()

        # Stage 1 (root -> root_frame)
        self.root_frame = ttk.Frame(self, padding=PADDING, style='red.TFrame')
        self.root_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Stage 2 (root_frame -> parent)
        self.tab_parent = ttk.Notebook(self.root_frame, style='red.TNotebook')
        self.next_button = ttk.Button(self.root_frame, text="Next", style='red.TButton')

        self.tab_parent.pack(expand=YES, fill='both', padx=6, pady=6)
        self.next_button.pack(anchor="se", padx=6)

        # Stage 3 (parent -> data - model - train - test)
        
        self.data_tab = ttk.Frame(self.tab_parent, padding=PADDING)
        self.model_tab = ttk.Frame(self.tab_parent, padding=PADDING)
        self.train_tab = ttk.Frame(self.tab_parent, padding=PADDING)
        self.test_tab = ttk.Frame(self.tab_parent, padding=PADDING)

        self.tab_parent.add(self.data_tab, text="Data")
        self.tab_parent.add(self.model_tab, text="Model")
        self.tab_parent.add(self.train_tab, text="Train")
        self.tab_parent.add(self.test_tab, text="Test")

        # Stage 4 (data_tab -> data_tab_frame)
        self.data_tab_frame = DataTab(self.data_tab)
        self.data_tab_frame.grid(column=0, row=0, sticky=(N,W,E), pady=24, padx=12)
        self.data_tab.columnconfigure(0, weight=1)
        self.data_tab.rowconfigure(0, weight=1)

        # Stage 4 (model_tab -> model_tab_frame)
        self.model_tab_frame = ModelTab(self.model_tab)
        self.model_tab_frame.grid(column=0, row=0, sticky=(N,W,E), pady=24, padx=12)
        self.model_tab.columnconfigure(0, weight=1)
        self.model_tab.rowconfigure(0, weight=1)

        # Stage 4 (train_tab -> train_tab_frame)
        self.train_tab_frame = TrainTab(self.train_tab)

        # Stage 4 (test_tab -> test_tab_frame)
        self.test_tab_frame = TestTab(self.test_tab)

window = Root()
window.mainloop()
