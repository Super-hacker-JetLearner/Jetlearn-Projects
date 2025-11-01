import cv2
import os
import numpy as np



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



font = cv2.FONT_ITALIC
color = [255, 255, 0]
thickness = 2
size = 2


Anna_photo = cv2.imread('/Users/s932172@aics.espritscholen.nl/Desktop/game development/cv development/Anna.png')
Julia_photo = cv2.imread('/Users/s932172@aics.espritscholen.nl/Desktop/game development/cv development/Julia.png')
Bartosz_photo = cv2.imread('/Users/s932172@aics.espritscholen.nl/Desktop/game development/cv development/Bartosz.png')


replace_with = Julia_photo


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
        
        name = names[prediction[0]]
        
        replace_image = cv2.resize(replace_with, (width, height))
        print(replace_image.shape)
        
        rows, columns = replace_image.shape[:2]
        gray_image = np.zeros((rows, columns), dtype=np.uint8)
        for row in range(rows):
            for col in range(columns):
                color, color, color = replace_image[row][col]
                gray_image[row][col] = color


        replace_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)
        
        frame[y:y+height, x:x+width] = replace_image
        
        
        
        
    key = cv2.waitKey(5)
    if key == 27:
        break
    
    
    
        
        
    cv2.imshow('video', frame)




cv2.destroyAllWindows()