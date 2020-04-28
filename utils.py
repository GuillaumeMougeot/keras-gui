from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from constants import *

class FileDialog(ttk.Frame):
    def __init__(self, *arg, mode='folder', textEntry="", **kw):
        super(FileDialog, self).__init__(*arg, **kw)
        assert mode in ['folder','file']

        self.filenameText = StringVar()
        self.set(textEntry)
        self.filename = ttk.Entry(self, textvariable=self.filenameText)
        self.filename.grid(column=1,row=1, sticky=(W,E))
        self.grid_columnconfigure(1, weight=1)

        self.command=self.openfolder if mode=='folder' else self.openfile
        self.button = ttk.Button(self,text="Browse", command=self.command)
        self.button.grid(column=2,row=1, sticky=(W))

    def set(self, text):
        # Set text entry
        self.filenameText.set(text)

    def openfolder(self):
        text = filedialog.askdirectory(initialdir =  ".", title = "Select A Folder")
        self.filenameText.set(text)
    
    def openfile(self):
        text = filedialog.askopenfilename(initialdir =  ".", title = "Select A File")
        self.filenameText.set(text)