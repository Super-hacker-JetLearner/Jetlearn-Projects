import os
import cv2



dataset_path = '/Users/s932172@aics.espritscholen.nl/Desktop/game development/cv development/6lesson/dataset'
person_name = 'Anna'

path = os.path.join(dataset_path, person_name)


for image_path in os.listdir(path):
    image = cv2.imread(os.path.join(path, image_path))
    cv2.imshow('image', image)
    cv2.waitKey(0)
    