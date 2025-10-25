import os
import cv2
import numpy
import time



haarcascade = '/Users/s932172@aics.espritscholen.nl/Desktop/game development/cv development/6lesson/haarcascade_frontalface_default.xml'

dataset_path = '/Users/s932172@aics.espritscholen.nl/Desktop/game development/cv development/6lesson/dataset'


id = 0
images = []
labels = []
names = {}

for _, directory, file in os.walk(dataset_path):
    for subdirectory in directory:
        names[id] = subdirectory
        for image in subdirectory:
            images.append(image)
            
            