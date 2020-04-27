from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from DataTab import DataTab
from TrainTab import TrainTab
from TestTab import TestTab
from constants import *

class Root(Tk):
    def __init__(self):
        # Stage 0 (root)
        super(Root, self).__init__()
        self.title("Classificator")
        self.geometry("720x480")
        self.minsize(480,360)
        self.iconbitmap("icons/main_icon.ico")
        self.config(background='#8296a7')

        # Stage 1 (root -> root_frame)
        self.root_frame = ttk.Frame(self, padding=PADDING)
        self.root_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Stage 2 (root_frame -> parent)
        self.tab_parent = ttk.Notebook(self.root_frame)

        # Stage 3 (parent -> data - model - train - test)
        self.data_tab = ttk.Frame(self.tab_parent, padding=PADDING)
        self.model_tab = ttk.Frame(self.tab_parent, padding=PADDING)
        self.train_tab = ttk.Frame(self.tab_parent, padding=PADDING)
        self.test_tab = ttk.Frame(self.tab_parent, padding=PADDING)

        self.tab_parent.add(self.data_tab, text="Data")
        self.tab_parent.add(self.model_tab, text="Model")
        self.tab_parent.add(self.train_tab, text="Train")
        self.tab_parent.add(self.test_tab, text="Test")

        self.tab_parent.pack(expand=YES, fill='both')

        # Stage 4 (data_tab -> model_tab_frame)
        self.data_tab_frame = DataTab(self.data_tab)
        self.data_tab_frame.pack(fill='x')

        # Stage 4 (train_tab -> train_tab_frame)
        self.train_tab_frame = TrainTab(self.train_tab)

        # Stage 4 (test_tab -> test_tab_frame)
        self.test_tab_frame = TestTab(self.test_tab)

window = Root()
window.mainloop()
