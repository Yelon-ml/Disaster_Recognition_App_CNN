import os
import sys
import importlib
from paths_creating import *
import numpy as np
from datetime import datetime
import json

import keras
from keras import layers
from keras import models
from keras import optimizers
from keras.models import load_model
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from keras import callbacks
from keras.callbacks import EarlyStopping
from keras.callbacks import ModelCheckpoint

import matplotlib.pyplot as plt

print(len(os.listdir(train_dir_c)), len(os.listdir(train_dir_e)), len(os.listdir(train_dir_f)), len(os.listdir(train_dir_w)))
print(len(os.listdir(validation_dir_c)), len(os.listdir(validation_dir_e)), len(os.listdir(validation_dir_f)), len(os.listdir(validation_dir_w)))
print(len(os.listdir(test_dir_c)), len(os.listdir(test_dir_e)), len(os.listdir(test_dir_f)), len(os.listdir(test_dir_w)))

class Model:

    def __init__(self):
        self.model = None
        self.model_path = 'best_model.h5'
        self.model_history_path = 'history'
        self.model_exists = os.path.exists(self.model_path)
        self.history_exists = os.path.exists(self.model_history_path)

    def create_model(self):
        if self.model_exists:
            self.model = load_model(self.model_path)
        else:
            self.model = models.Sequential()
            self.model.add(layers.Conv2D(32, (3, 3), activation = 'relu', input_shape= (180, 180, 3)))
            self.model.add(layers.MaxPooling2D((2, 2)))
            self.model.add(layers.Conv2D(64, (3, 3), activation = 'relu'))
            self.model.add(layers.MaxPooling2D((2, 2)))
            self.model.add(layers.Conv2D(128, (3, 3), activation= 'relu'))
            self.model.add(layers.MaxPooling2D((2, 2)))
            self.model.add(layers.Conv2D(128, (3, 3), activation= 'relu'))
            self.model.add(layers.MaxPooling2D((2, 2)))
            self.model.add(layers.Conv2D(256, (3, 3), activation = 'relu'))
            self.model.add(layers.MaxPooling2D((2, 2)))
            self.model.add(layers.Flatten())
            self.model.add(layers.Dropout(0.3))
            self.model.add(layers.Dense(512, activation = 'relu'))
            self.model.add(layers.Dense(4, activation = 'softmax'))

    def summary(self):
        return self.model.summary()

    def compile(self):
        if not self.model_exists:
            self.model.compile(optimizer=optimizers.RMSprop(lr=1e-4), loss='categorical_crossentropy', metrics=['acc'])
            print("Model compiled.")
        else:
            print("\n\nModel found, no compilation needed.\n\n")

    def data_generator(self):
        self.train_datagen = ImageDataGenerator(rescale= 1./255,
                                    rotation_range= 40,
                                    width_shift_range= .2,
                                    height_shift_range= .2,
                                    shear_range= .2,
                                    zoom_range= .2,
                                    horizontal_flip= True)

        self.test_datagen = ImageDataGenerator(rescale= 1./255)

        self.train_generator = self.train_datagen.flow_from_directory(train_dir,
                                                    target_size= (180, 180),
                                                    batch_size=32,
                                                    class_mode='categorical')

        self.validation_generator = self.test_datagen.flow_from_directory(validation_dir,
                                                    target_size=(180, 180),
                                                    batch_size=32,
                                                    class_mode='categorical')



    def train(self):

        self.logdir = "DisasterModel\\Logs" + datetime.now().strftime("%Y%m%d-%H%M%S")
        self.tensorboard_callback = keras.callbacks.TensorBoard(log_dir = self.logdir, histogram_freq=0, write_graph=True, write_images=True)
        self.es = EarlyStopping(monitor='val_acc', mode='max', verbose=1, patience=6)
        self.mc = ModelCheckpoint('best_model.h5', monitor='val_acc', mode='max', verbose=1, save_best_only=True)

        self.history = None

        if self.history_exists:
            with open(self.model_history_path, 'r') as json_file:
                self.history = json.load(json_file)
                print("\n\nThe history file has been found, no training needed.\n")
        else:
            self.history = self.model.fit_generator(self.train_generator,
                                                    steps_per_epoch=150,
                                                    epochs=100,
                                                    validation_data=self.validation_generator,
                                                    validation_steps=50,
                                                    callbacks=[self.es, self.mc, self.tensorboard_callback])
            print("\n\nModel has been trained.\n\n")


if __name__ == "__main__":
    disaster_model = Model()
    disaster_model.create_model()
    disaster_model.summary()
    disaster_model.compile()
    disaster_model.data_generator()
    disaster_model.train()
