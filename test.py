from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

import numpy as np

class Testing():
    def __init__(self, model_name):
        print(model_name)
        self.model = load_model(model_name)

    def test_image(self, filename):
        self.image = image.load_img(filename, target_size=(150,150))
        self.image = image.img_to_array(self.image)/255.
        self.image = np.expand_dims(self.image, 0)
        self.image,_,_=self.model._standardize_user_data(self.image)
        return round(self.model.predict(self.image[0])[0][0])
    
