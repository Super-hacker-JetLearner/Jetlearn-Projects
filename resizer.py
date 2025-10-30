import os
import cv2

dataset_path = '/Users/s932172@aics.espritscholen.nl/Desktop/game development/cv development/6lesson/dataset'




for _, subdirectories, file in os.walk(dataset_path):
    for subdirectory in subdirectories:

        for image_path in os.listdir(os.path.join(dataset_path, subdirectory)):
            print(image_path)
            image = cv2.imread(os.path.join(dataset_path, subdirectory, image_path))
            image = cv2.resize(image, (300, 300))
            cv2.imwrite(os.path.join(dataset_path, subdirectory, image_path), image)




            
