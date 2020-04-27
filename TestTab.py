from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from test import Testing
from utils import FileDialog
from constants import *

class TestTab(ttk.Frame):
    def __init__(self, *arg, **kw):
        super(TestTab, self).__init__(*arg, **kw)
        self.pack(fill='x')

        # Stage 5 (sub_test -> fd1 - fd2 - testButton)
        self.label1 = ttk.Label(self, text="Select a .h5 file containing a trained model")
        self.label1.pack(anchor='w')
        self.fd1 = FileDialog(self, mode='file')
        self.fd1.pack(fill='both',anchor='w')

        self.empty_space1 = ttk.Label(self, text="")
        self.empty_space1.pack()

        self.label2 = ttk.Label(self, text="Select an image to predict")
        self.label2.pack(anchor='w')
        self.fd2 = FileDialog(self, mode='file')
        self.fd2.pack(fill='both',anchor='w')

        self.empty_space2 = ttk.Label(self, text="")
        self.empty_space2.pack()

        self.testButton = ttk.Button(
            self,
            text = "Test!",
            padding=PADDING,
            command=self.test_image)
        self.testButton.pack(fill='both')
    
    def test_image(self):
        # Predict test class
        self.test = Testing(self.fd1.filenameText.get())
        predicted_class = self.test.test_image(self.fd2.filenameText.get())

        # Display test class
        self.label_pred = ttk.Label(self, text="Predicted class: {:.4f}".format(predicted_class))
        self.label_pred.pack(fill='both')
