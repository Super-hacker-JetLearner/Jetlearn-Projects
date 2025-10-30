import os
import cv2
import numpy
import time



haarcascade = '/Users/s932172@aics.espritscholen.nl/Desktop/game development/cv development/6lesson/haarcascade_frontalface_default.xml'

dataset_path = '/Users/s932172@aics.espritscholen.nl/Desktop/game development/cv development/6lesson/dataset'

person_path = 'Tomasz'

path = os.path.join(dataset_path, person_path)

if not os.path.isdir(path):
    os.mkdir(path)
    

cascade_classifier = cv2.CascadeClassifier(haarcascade)
webcam = cv2.VideoCapture(0)

count = 1
while count < 50:
    is_img, img = webcam.read()
    if not is_img:
        print('no image')
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = cascade_classifier.detectMultiScale(img, 1.3, 5)
    for x, y, width, height in faces:
        img = cv2.rectangle(img, (x, y), (x+width, y+height), (255, 0, 0), 5)
        
        count += 1
        cropped_image = img[y:y+height, x:x+width]

        cv2.imwrite('% s/% s.png'%(path, count), cropped_image)
        
        

    cv2.imshow('image', img)
    cv2.waitKey(0)
    
    

