from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os
from PIL import Image, ImageTk

from utils import FileDialog
from constants import *

class DataSelection(ttk.LabelFrame):
    def __init__(self, *arg, **kw):
        super(DataSelection, self).__init__(*arg, **kw)

        # Define elements
        ## Train folder
        self.label1 = ttk.Label(self, text="Select a folder containing training images", anchor="sw", background='white')
        self.fd1 = FileDialog(self, mode='folder', textEntry='data/train')

        ## Test folder
        self.label2 = ttk.Label(self, text="Select a folder containing testing images", anchor="sw", background='white')
        self.fd2 = FileDialog(self, mode='folder', textEntry='data/test')

        ## Print class names
        self.print_class_names_button = ttk.Button(self,text="Print class names", command=self.print_class_names)
        self.grid_frame=ttk.Frame(self)
        self.label_class_names = ttk.Label(self.grid_frame, text="Classes names: ", background='white')
        self.tree_view = ttk.Treeview(self.grid_frame, show='tree')
        self.list_class_names = []

        ## Image
        load = Image.open(PATH_IMG_SELECT)
        render = ImageTk.PhotoImage(load)
        self.label_image_data_selection = ttk.Label(self, image=render, anchor="center", background='white')
        self.label_image_data_selection.image=render

        # Position elements
        padx=5
        self.label1.grid(column=0, row=0, sticky=W, padx=padx)
        self.fd1.grid(column=0, row=1, sticky=(W,E), padx=padx)
        self.label2.grid(column=0,row=2, sticky=W, padx=padx)
        self.fd2.grid(column=0,row=3, sticky=(W,E), padx=padx)
        self.print_class_names_button.grid(column=0,row=4, sticky=(W,E), padx=padx)
        self.grid_frame.grid(column=0,row=5, sticky=(W,E), padx=padx)
        self.label_image_data_selection.grid(column=1,row=0,rowspan=6,sticky=(W,E,S,N))

        # Configure columns
        self.columnconfigure(0, weight=10)
        self.columnconfigure(1, weight=1)
        # for i in range(2):
        #     self.columnconfigure(i, weight=1)
        for i in range(6):
            self.rowconfigure(i, weight=1)
        

    def get_train_foldername(self):
        return self.fd1.filenameText.get()
    
    def get_test_foldername(self):
        return self.fd2.filenameText.get()

    def print_class_names(self):
        train_foldername = self.get_train_foldername()
        test_foldername = self.get_test_foldername()

        if os.listdir(train_foldername)==os.listdir(test_foldername):
            self.label_class_names.grid(column=0, row=0)

            if os.listdir(train_foldername)!=self.list_class_names:
                self.list_class_names=os.listdir(train_foldername)
                tree_height = len(self.list_class_names) if len(self.list_class_names)<=5 else 5
                self.tree_view.configure(height=tree_height)
                
                for element in self.list_class_names:
                    self.tree_view.insert('','end',text=element)
                self.tree_view.grid(column=1,row=0)
        else:
            messagebox.showerror(title="Unmatching sub-folders architecture", message="Training folder and testing folder should have the same sub-folder architecture.")

class DataAugmentation(ttk.LabelFrame):
    def __init__(self, *arg, **kw):
        super(DataAugmentation, self).__init__(*arg, **kw)

        center_sample_label = ttk.Label(self,text="Center sample: ")
        center_sample_label.grid(column=0, row=0)
        center_sample_cb = ttk.Checkbutton(self, text="")
        center_sample_cb.state(['!alternate'])
        center_sample_cb.grid(column=1, row=0)

class DataTab(ttk.Frame):
    def __init__(self, *arg, **kw):
        super(DataTab, self).__init__(*arg, **kw)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.lf_data_selection = DataSelection(self, text="Data selection")
        # self.lf_data_selection.pack(fill='x')
        self.lf_data_selection.grid(column=0,row=0,sticky=(N,W,E), pady=3)


        self.lf_data_augmentation = DataAugmentation(self, text="Data augmentation")
        # self.lf_data_augmentation.pack(fill='x')
        self.lf_data_augmentation.grid(column=0,row=1,sticky=(N,W,E), pady=3)


        # TODO:
        # Check if the two folders have the same folder architecture
        # assert os.listdir(train_foldername)==os.listdir(test_foldername), "[Error] The training folder architecture should be the same as the testing one.\nTraining architecture: {}\nTesting architecture: {}".format(train_foldername, test_foldername)

