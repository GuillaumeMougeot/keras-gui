from tkinter import *
from tkinter import ttk
# from tkinter import dnd # for drag and drop tool
# from tkinter import filedialog
# from tkinter import messagebox
# import os
# from PIL import Image, ImageTk

# from utils import FileDialog
# from constants import *
# import settings

class ModelBuilding(ttk.LabelFrame):
    def __init__(self, *arg, **kw):
        super(ModelBuilding, self).__init__(*arg, **kw)

        # Create widgets
        choose_model_label = ttk.Label(self,text="Please choose a model: ", anchor="w")
        choose_model_values = ["binary"]
        self.choose_model_stringvar = StringVar()
        choose_model_combobox = ttk.Combobox(self, textvariable=self.choose_model_stringvar, values=choose_model_values, width=20)

        # Position widgets
        choose_model_label.grid(column=0, row=0, sticky=(W,E))
        choose_model_combobox.grid(column=1, row=0, sticky=(W))

        # Configure grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=10)
        self.rowconfigure(0, weight=1)

class ModelCompilation(ttk.LabelFrame):
    def __init__(self, *arg, **kw):
        super(ModelCompilation, self).__init__(*arg, **kw)

        optimizer_label = ttk.Label(self,text="Please choose an optimizer: ", anchor="w")
        optimizer_values = ["adam", "rmsprop", "sgd"]
        self.optimizer_stringvar = StringVar()
        optimizer_combobox = ttk.Combobox(self, textvariable=self.optimizer_stringvar, values=optimizer_values, width=20)

        # Position widgets
        optimizer_label.grid(column=0, row=0, sticky=(W,E))
        optimizer_combobox.grid(column=1, row=0, sticky=(W))

        # Configure grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=10)
        self.rowconfigure(0, weight=1)


class ModelTab(ttk.Frame):
    def __init__(self, *arg, **kw):
        super(ModelTab, self).__init__(*arg, **kw)

        self.lf_data_selection = ModelBuilding(self, text="Model building", padding=[10,10,10,10])
        self.lf_data_augmentation = ModelCompilation(self, text="Model compilation", padding=[10,10,10,10])

        self.lf_data_selection.grid(column=0,row=0,sticky=(N,W,E), pady=3)
        self.lf_data_augmentation.grid(column=0,row=1,sticky=(N,W,E), pady=3)
    
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
