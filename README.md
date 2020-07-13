# Disaster_Recognition_App_CNN

In this project I would like to present the application based on the convolutional neural network, able to recognition a natural disaster like: cyclone, flood, earthquake and wildfire.

The data for training, validation and testing, that contains almost 4,500 images, has been downloaded from the below:
https://drive.google.com/file/d/1NvTyhUsrFbL91E10EPm38IjoCg6E2c6q/view

The project contains 4 python files, used for:
- paths_creating.py - creating all neccessary paths on a drive
- images_copying.py - splitting images into the train/validation/test subfolders
- model.py - the main model (based on keras cnn)
- model_interface.py - the interface written using TkInter to operate the model on a new images.

Moreover, in the repository one can find the trained model  - best_model.h5 (together with the history file, which can be used to run the model_interface.py without any further trainin), screens that can be found below and some sample images that the model recognizes.


![App screen](https://github.com/Yelon-ml/Disaster_Recognition_App_CNN/blob/master/app%20screen/app1.PNG)
![App screen](https://github.com/Yelon-ml/Disaster_Recognition_App_CNN/blob/master/app%20screen/app2.PNG)
