from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from train import Training
from utils import FileDialog
from constants import *

class TrainTab(ttk.Frame):
    def __init__(self, *arg, **kw):
        super(TrainTab, self).__init__(*arg, **kw)
        self.pack(fill='x')

        # Stage 5 (sub_train -> fd1 - fd2 - trainButton)
        self.label1 = ttk.Label(self, text="Select folder containing training images")
        self.label1.pack(anchor='w')
        self.fd1 = FileDialog(self, mode='folder')
        self.fd1.filenameText.set('data/train')
        self.fd1.pack(fill='both',anchor='w')

        self.empty_space1 = ttk.Label(self, text="")
        self.empty_space1.pack()

        self.label2 = ttk.Label(self, text="Select folder containing testing images")
        self.label2.pack(anchor='w')
        self.fd2 = FileDialog(self, mode='folder')
        self.fd2.filenameText.set('data/test')
        self.fd2.pack(fill='both',anchor='w')

        self.empty_space2 = ttk.Label(self, text="")
        self.empty_space2.pack()

        self.trainButton = ttk.Button(
            self,
            text = "Train!",
            padding=PADDING,
            command=self.train_model)
        self.trainButton.pack(fill='both')
        
    def train_model(self):
        nbof_epochs = 30
        batch_size = 64
        nbof_images = 2000
        nbof_validation_images = 1000

        nbof_steps = nbof_images // batch_size
        nbof_validation_steps = nbof_validation_images // batch_size

        # TODO: check validity of training and testing folders
        #  - same number of classes
        # TODO: save class names
        # TODO: display training infos

        # "Training..." label
        self.label_progress_bar_steps = ttk.Label(self, text="Training...\nStep {:d}/{:d}".format(0,nbof_steps))
        self.label_progress_bar_steps.pack(anchor='w')

        # Create a progress bar for steps
        self.progress_bar_steps = ttk.Progressbar(self, orient=HORIZONTAL, maximum=nbof_steps, mode='determinate')
        self.progress_bar_steps.pack(fill='both')

        # Epoch label
        self.label_progress_bar_epochs = ttk.Label(self, text="Epoch {:d}/{:d}".format(0,nbof_epochs))
        self.label_progress_bar_epochs.pack(anchor='w')

        # Create a progress bar for epochs
        self.progress_bar_epochs = ttk.Progressbar(self, orient=HORIZONTAL, maximum=nbof_epochs, mode='determinate')
        self.progress_bar_epochs.pack(fill='both')

        # Create display for training info
        self.display_train_info = ttk.Label(self, font=("Courier", 10), text="{:<20}{:<20}{:<20}{:<20}\n{:<20.4f}{:<20.4f}{:<20.4f}{:<20.4f}".format(
            "Training Loss", "Training Accuracy", "Testing Loss", "Testing Accuracy",0,0,0,0))
        self.display_train_info.pack(fill='both')

        # Update the frame
        self.update()

        # Initiate the training
        self.train = Training(
            self.fd1.filenameText.get(),
            self.fd2.filenameText.get(),
            batch_size)

        train_loss  = 0
        train_acc   = 0
        test_loss   = 0
        test_acc    = 0

        def update_display(train_loss,train_acc,test_loss,test_acc):
            self.display_train_info['text']="{:<20}{:<20}{:<20}{:<20}\n{:<20.4f}{:<20.4f}{:<20.4f}{:<20.4f}".format(
                "Training Loss", "Training Accuracy", "Testing Loss", "Testing Accuracy",train_loss,train_acc,test_loss,test_acc)

        # Run the training
        for epoch in range(nbof_epochs):
            # Train on one epoch
            self.label_progress_bar_steps['text']="Training...\nStep {:d}/{:d}".format(0,nbof_steps)
            self.progress_bar_steps['value']=0
            self.progress_bar_steps['maximum']=nbof_steps
            self.progress_bar_steps.update()
            for step in range(nbof_steps):
                train_loss, train_acc = self.train.train_on_batch()

                self.label_progress_bar_steps['text']="Training...\nStep {:d}/{:d}".format(step+1,nbof_steps)
                self.progress_bar_steps['value']=step+1
                update_display(train_loss,train_acc,test_loss,test_acc)
                self.progress_bar_steps.update()

            # Validate
            self.label_progress_bar_steps['text']="Validation...\nStep {:d}/{:d}".format(0,nbof_validation_steps)
            self.progress_bar_steps['value']=0
            self.progress_bar_steps['maximum']=nbof_validation_steps
            self.progress_bar_steps.update()
            test_loss   = 0
            test_acc    = 0
            for step in range(nbof_validation_steps):
                crt_test_loss, crt_test_acc = self.train.test_on_batch()
                test_loss, test_acc = test_loss+crt_test_loss, test_acc+crt_test_acc

                self.label_progress_bar_steps['text']="Validation...\nStep {:d}/{:d}".format(step+1,nbof_validation_steps)
                self.progress_bar_steps['value']=step+1
                self.progress_bar_steps.update()
        
            test_loss   /= nbof_validation_steps
            test_acc    /= nbof_validation_steps
            update_display(train_loss,train_acc,test_loss,test_acc)
            
            self.label_progress_bar_epochs['text']="Epoch {:d}/{:d}".format(epoch+1,nbof_epochs)
            self.progress_bar_epochs['value']=epoch+1
            self.progress_bar_epochs.update()
        
        self.train.save_model(model_name='models/two_try.h5')

        self.label_end = ttk.Label(self, text="Training done! The model can now be tested in the \"Test\" tab.")
        self.label_end.pack(anchor='w')

