import os
import cv2
import numpy as np
import time



haarcascade = '/Users/s932172@aics.espritscholen.nl/Desktop/game development/cv development/6lesson/haarcascade_frontalface_default.xml'

dataset_path = '/Users/s932172@aics.espritscholen.nl/Desktop/game development/cv development/6lesson/dataset'


id = 0
images = []
labels = []
names = {}

for _, subdirectories, file in os.walk(dataset_path):
    for subdirectory in subdirectories:
        names[id] = subdirectory

        
        for image_path in os.listdir(os.path.join(dataset_path, subdirectory)):
            image = cv2.imread(os.path.join(dataset_path, subdirectory, image_path), 0)
            images.append(image)
            labels.append(id)
        
        
            
        id += 1




images = np.array(images)
labels = np.array(labels)




model = cv2.face.LBPHFaceRecognizer_create()
model.train(images, labels)

print('trained')


cascade_classifier = cv2.CascadeClassifier(haarcascade)
print('cascade')

webcam = cv2.VideoCapture(0)
print('webcam')





while True:
    is_frame, frame = webcam.read()
    if not is_frame:
        print('no frame')
        
        
    
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = cascade_classifier.detectMultiScale(grayscale, 1.5, 7)
    for x, y, width, height in faces:
        frame = cv2.rectangle(frame, (x, y), (x+width, y+height), (255, 0, 0), 3)
        cropped_image = grayscale[y:y+height, x:x+width]
        
        cropped_image = cv2.resize(cropped_image, (300, 300))
        
        prediction = model.predict(cropped_image)
        print(names[prediction[0]], prediction[1])
        
        
        
        
    key = cv2.waitKey(5)
    if key == 27:
        break
    
    
    
        
        
    cv2.imshow('video', frame)




cv2.destroyAllWindows()


"homework, change images in folders, make program to use haarcascade to draw rectangles around images, test and improve this"