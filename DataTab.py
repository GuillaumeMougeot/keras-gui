from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os

from utils import FileDialog
from constants import *

class DataSelection(ttk.LabelFrame):
    def __init__(self, *arg, **kw):
        super(DataSelection, self).__init__(*arg, **kw)

        self.label1 = ttk.Label(self, text="Select a folder containing training images")
        self.label1.pack(anchor='w')
        self.fd1 = FileDialog(self, mode='folder')
        self.fd1.filenameText.set('data/train')
        self.fd1.pack(fill='both',anchor='w')

        # self.empty_space = ttk.Label(self, text="")
        # self.empty_space.pack()

        self.label2 = ttk.Label(self, text="Select a folder containing testing images")
        self.label2.pack(anchor='w')
        self.fd2 = FileDialog(self, mode='folder')
        self.fd2.filenameText.set('data/test')
        self.fd2.pack(fill='both',anchor='w')
    
    def get_train_foldername(self):
        return self.fd1.filenameText.get()
    
    def get_test_foldername(self):
        return self.fd2.filenameText.get()

class DataTab(ttk.Frame):
    def __init__(self, *arg, **kw):
        super(DataTab, self).__init__(*arg, **kw)

        self.lf_data_selection = DataSelection(self, text="Data selection")
        self.lf_data_selection.pack(fill='x')

        
        train_foldername = self.lf_data_selection.get_train_foldername()
        test_foldername = self.lf_data_selection.get_test_foldername()
        if os.listdir(train_foldername)==os.listdir(test_foldername):
            # TODO: print class names into a grid

        # TODO:
        # Check if the two folders have the same folder architecture
        # assert os.listdir(train_foldername)==os.listdir(test_foldername), "[Error] The training folder architecture should be the same as the testing one.\nTraining architecture: {}\nTesting architecture: {}".format(train_foldername, test_foldername)

