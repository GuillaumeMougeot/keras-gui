from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os
from PIL import Image, ImageTk

from utils import FileDialog
from constants import *
import settings

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
        self.label_class_names = ttk.Label(self.grid_frame, text="Classes names: ", background='white', anchor="e")
        self.tree_view = ttk.Treeview(self.grid_frame, show='tree')
        self.list_class_names = []

        ## Image
        load = Image.open(PATH_IMG_SELECT)
        render = ImageTk.PhotoImage(load)
        self.label_image_data_selection = ttk.Label(self, image=render, anchor="center", background='white')
        self.label_image_data_selection.image=render

        # Position elements
        self.label1.grid(column=0, row=0, sticky=W)
        self.fd1.grid(column=0, row=1, sticky=(W,E))
        self.label2.grid(column=0,row=2, sticky=W)
        self.fd2.grid(column=0,row=3, sticky=(W,E))
        self.print_class_names_button.grid(column=0,row=4, sticky=(W,E))
        self.grid_frame.grid(column=0,row=5, sticky=(W,E))
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
            # Configure class name grid
            self.grid_frame.columnconfigure(0,weight=1)
            self.grid_frame.columnconfigure(1,weight=1)
            self.grid_frame.rowconfigure(0,weight=1)

            # Position label
            self.label_class_names.grid(column=0, row=0, sticky=(W,E))

            if os.listdir(train_foldername)!=self.list_class_names:
                self.list_class_names=os.listdir(train_foldername)
                tree_height = len(self.list_class_names) if len(self.list_class_names)<=5 else 5
                self.tree_view.configure(height=tree_height)
                
                for element in self.list_class_names:
                    self.tree_view.insert('','end',text=element)
                self.tree_view.grid(column=1, row=0, sticky=(W,E))
        else:
            messagebox.showerror(title="Unmatching sub-folders architecture", message="Training folder and testing folder should have the same sub-folder architecture.")

class DataAugmentation(ttk.LabelFrame):
    def __init__(self, *arg, **kw):
        super(DataAugmentation, self).__init__(*arg, **kw)

        # Create elements
        center_sample_label = ttk.Label(self,text="Center sample: ", anchor="w")
        self.center_sample_cb = ttk.Checkbutton(self, text="")
        self.center_sample_cb.state(['!alternate'])

        normalize_sample_label = ttk.Label(self,text="Normalize sample: ", anchor="w")
        self.normalize_sample_cb = ttk.Checkbutton(self, text="")
        self.normalize_sample_cb.state(['!alternate'])

        rotation_range_label = ttk.Label(self,text="Rotation range: ", anchor="w")
        self.rotation_range_spinval = DoubleVar()
        rotation_range_spinbox = ttk.Spinbox(self, from_=0., to=1., textvariable=self.rotation_range_spinval, increment=0.1, width=5)

        width_shift_label = ttk.Label(self,text="Width shift range: ", anchor="w")
        self.width_shift_spinval = DoubleVar()
        width_shift_spinbox = ttk.Spinbox(self, from_=0., to=1., textvariable=self.width_shift_spinval, increment=0.1, width=5)

        height_shift_label = ttk.Label(self,text="Height shift range: ", anchor="w")
        self.height_shift_spinval = DoubleVar()
        height_shift_spinbox = ttk.Spinbox(self, from_=0., to=1., textvariable=self.height_shift_spinval, increment=0.1, width=5)

        zoom_label = ttk.Label(self,text="Zoom range: ", anchor="w")
        self.zoom_spinval = DoubleVar()
        zoom_spinbox = ttk.Spinbox(self, from_=0., to=1., textvariable=self.zoom_spinval, increment=0.1, width=5)

        channel_shift_label = ttk.Label(self,text="Channel shift range: ", anchor="w")
        self.channel_shift_spinval = DoubleVar()
        channel_shift_spinbox = ttk.Spinbox(self, from_=0., to=1., textvariable=self.channel_shift_spinval, increment=0.1, width=5)

        fill_mode_label = ttk.Label(self,text="Fill mode: ", anchor="w")
        fill_mode_values = ["constant", "nearest", "reflect", "wrap"]
        self.fill_mode_stringvar = StringVar()
        fill_mode_combobox = ttk.Combobox(self, textvariable=self.fill_mode_stringvar, values=fill_mode_values, width=10)

        horizontal_flip_label = ttk.Label(self,text="Horizontal flip: ", anchor="w")
        self.horizontal_flip_cb = ttk.Checkbutton(self, text="")
        self.horizontal_flip_cb.state(['!alternate'])

        vertical_flip_label = ttk.Label(self,text="Vertical flip: ", anchor="w")
        self.vertical_flip_cb = ttk.Checkbutton(self, text="")
        self.vertical_flip_cb.state(['!alternate'])

        # Position elements
        center_sample_label.grid(column=0, row=0, sticky=(W,E))
        self.center_sample_cb.grid(column=1, row=0, sticky=(W))

        normalize_sample_label.grid(column=0, row=1, sticky=(W,E))
        self.normalize_sample_cb.grid(column=1, row=1, sticky=(W))

        rotation_range_label.grid(column=0, row=2, sticky=(W,E))
        rotation_range_spinbox.grid(column=1, row=2, sticky=(W))

        width_shift_label.grid(column=0, row=3, sticky=(W,E))
        width_shift_spinbox.grid(column=1, row=3, sticky=(W))

        height_shift_label.grid(column=0, row=4, sticky=(W,E))
        height_shift_spinbox.grid(column=1, row=4, sticky=(W))

        zoom_label.grid(column=0, row=5, sticky=(W,E))
        zoom_spinbox.grid(column=1, row=5, sticky=(W))

        channel_shift_label.grid(column=0, row=6, sticky=(W,E))
        channel_shift_spinbox.grid(column=1, row=6, sticky=(W))

        fill_mode_label.grid(column=0, row=7, sticky=(W,E))
        fill_mode_combobox.grid(column=1, row=7, sticky=(W))

        horizontal_flip_label.grid(column=0, row=8, sticky=(W,E))
        self.horizontal_flip_cb.grid(column=1, row=8, sticky=(W))

        vertical_flip_label.grid(column=0, row=9, sticky=(W,E))
        self.vertical_flip_cb.grid(column=1, row=9, sticky=(W))

        # Configure grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=10)
        for i in range(10):
            self.rowconfigure(i, weight=1)
    
    def get_checkbutton_val(self, checkbutton):
        # Return True or False if selected or not
        if len(checkbutton.state())==0:
            return False 
        else:
            return checkbutton.state()[0]=='selected'

    def update_settings(self):
        settings.samplewise_center = self.get_checkbutton_val(self.center_sample_cb)
        settings.samplewise_std_normalization = self.get_checkbutton_val(self.normalize_sample_cb)
        settings.rotation_range = self.rotation_range_spinval.get()
        settings.width_shift_range = self.width_shift_spinval.get()
        settings.height_shift_range = self.height_shift_spinval.get()
        settings.zoom_range = self.zoom_spinval.get()
        settings.channel_shift_range = self.channel_shift_spinval.get()
        if self.fill_mode_stringvar.get()=="":
            settings.fill_mode = "nearest"
        else:
            settings.fill_mode = self.fill_mode_stringvar.get()
        settings.horizontal_flip = self.get_checkbutton_val(self.horizontal_flip_cb)
        settings.vertical_flip = self.get_checkbutton_val(self.vertical_flip_cb)

# The actual widget that could have been used here is ttk.Panedwindow
class DataTab(ttk.Frame):
    def __init__(self, *arg, **kw):
        super(DataTab, self).__init__(*arg, **kw)

        self.lf_data_selection = DataSelection(self, text="Data selection", padding=[10,10,10,10])
        self.lf_data_augmentation = DataAugmentation(self, text="Data augmentation", padding=[10,10,10,10])
        self.tmp_button = ttk.Button(self, text="Apply", command=self.update_settings)

        self.lf_data_selection.grid(column=0,row=0,sticky=(N,W,E), pady=3)
        self.lf_data_augmentation.grid(column=0,row=1,sticky=(N,W,E), pady=3)
        self.tmp_button.grid(column=0,row=2,sticky=(N,W,E))
    
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)


        # TODO:
        # Check if the two folders have the same folder architecture
        # assert os.listdir(train_foldername)==os.listdir(test_foldername), "[Error] The training folder architecture should be the same as the testing one.\nTraining architecture: {}\nTesting architecture: {}".format(train_foldername, test_foldername)

    def update_settings(self):
        self.lf_data_augmentation.update_settings()

