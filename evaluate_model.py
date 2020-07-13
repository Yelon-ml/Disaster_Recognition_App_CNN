from paths_creating import *
import keras
from keras import models
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator

class Evaluation:

    def __init__(self):

        self.best_model = 'best_model.h5'
        self.model = load_model(self.best_model)

        self.test_datagen = ImageDataGenerator(rescale=1./255)
        self.test_generator = test_datagen.flow_from_directory(test_dir, target_size=(180, 180), batch_size=1)

        print("\n\nLength of the test batch: {}.".format(len(self.test_generator))) # [] batch_nr, [] data/labels, [] img_nr, [][] dims, [] channels

        self.loss_test, self.acc_test = self.model.evaluate(self.test_generator)

        print("\n\nThe test accuracy is equal to {},\nwhile the loss on the test batch is equal to {}.".format(self.acc_test, self.loss_test))

if __name__ == "__main__":
    eval = Evaluation()
