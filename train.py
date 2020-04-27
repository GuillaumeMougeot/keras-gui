import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Activation, MaxPooling2D, Dense, GlobalAveragePooling2D, Dropout

class Training():
    def __init__(self, folder1, folder2, batch_size):
        # Create the model
        self.model = self.build_model()

        self.batch_size = batch_size

        # Data generators
        self.train_datagen = ImageDataGenerator(
                rescale=1./255,
                shear_range=0.2,
                zoom_range=0.2,
                horizontal_flip=True)

        self.test_datagen = ImageDataGenerator(rescale=1./255)

        self.train_generator = self.train_datagen.flow_from_directory(
                folder1,  
                target_size=(150, 150),  # all images will be resized to 150x150
                batch_size=self.batch_size,
                class_mode='binary')  # since we use binary_crossentropy loss, we need binary labels

        self.validation_generator = self.test_datagen.flow_from_directory(
                folder2,
                target_size=(150, 150),
                batch_size=self.batch_size,
                class_mode='binary')

    def build_model(self):
        model = Sequential()
        model.add(Conv2D(32, (3, 3)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Conv2D(32, (3, 3)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Conv2D(64, (3, 3)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(GlobalAveragePooling2D())
        model.add(Dense(64))
        model.add(Activation('relu'))
        model.add(Dropout(0.5))
        model.add(Dense(1))
        model.add(Activation('sigmoid'))

        model.compile(loss='binary_crossentropy',
                    optimizer='rmsprop',
                    metrics=['accuracy'])
        
        return model

    def standardize_data(self,x,y):
        x = tf.convert_to_tensor(x, dtype=tf.float32)*2-1
        x = tf.reshape(x, (-1,150,150,3))
        y = tf.convert_to_tensor(y, dtype=tf.float32)
        y = tf.reshape(y, (-1, 1))
        return x,y

    def train_on_batch(self):
        (x,y) = next(self.train_generator)
        return self.model.train_on_batch(x,y)
    
    def test_on_batch(self):
        (x,y) = next(self.validation_generator)
        return self.model.test_on_batch(x,y)
    
    def save_model(self, model_name):
        self.model.save(model_name) 
