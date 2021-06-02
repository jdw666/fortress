from django.apps import AppConfig
import numpy as np
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import to_categorical

class AiConfig(AppConfig):
    def __init__(self, path):
        # load model to memory
        self.model = load_model(path)

    def predictNum(self, index):
        _,(test_images, test_labels) = mnist.load_data()
        #plt.imshow(np.reshape(test_images[index],(28,28)))
        test_images = test_images.reshape((10000, 28 * 28))
        test_images = test_images.astype('float32') / 255
        test_labels = to_categorical(test_labels)
        # 应用
        result = self.model.predict_classes(np.expand_dims(test_images[index], 0))
        return result

