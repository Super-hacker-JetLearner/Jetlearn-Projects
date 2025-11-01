import os
import cv2


haarcascade = '/Users/s932172@aics.espritscholen.nl/Desktop/game development/cv development/6lesson/haarcascade_frontalface_default.xml'




webcam = cv2.VideoCapture(0)
cascade_classifier = cv2.CascadeClassifier(haarcascade)
print('cascade')


while True:
    is_frame, frame = webcam.read()
    print('frame')
    if not is_frame:
        print('no frame')
        

    
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = cascade_classifier.detectMultiScale(grayscale, 1.1, 5)
    for x, y, width, height in faces:
        frame = cv2.rectangle(frame, (x, y), (x+width, y+height), (255, 0, 0), 3)
        
        
        
        
    key = cv2.waitKey(5)
    if key == 27:
        break
    
    
    cv2.imshow('video', frame)
    
    
    
cv2.destroyAllWindows()