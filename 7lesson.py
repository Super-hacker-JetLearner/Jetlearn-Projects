import cv2
import os


car_video_path = '/Users/s932172@aics.espritscholen.nl/Desktop/game development/cv development/cars1.mp4'


car_video = cv2.VideoCapture(car_video_path)


cars_classifier_path = '/Users/s932172@aics.espritscholen.nl/Desktop/game development/cv development/cars.xml'

cars_classifier = cv2.CascadeClassifier(cars_classifier_path)

is_frame = True

while is_frame:
    is_frame, frame = car_video.read()
    if not is_frame:
        print('no frame')
        
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = cars_classifier.detectMultiScale(grayscale, 1.07, 4)
    for x, y, width, height in cars:
        cv2.rectangle(frame, (x, y), (x+width, y+width), [255, 0, 0], 3)
        
    num_cars = len(cars)
    
    frame = cv2.putText(frame, f'num cars: {num_cars}', (300, 50), cv2.FONT_ITALIC, 2, (255, 0, 0), 2, cv2.LINE_AA)
    
    cv2.imshow('video', frame)
    
    key = cv2.waitKey(5)
    if key == 27:
        break
    
    

    
cv2.destroyAllWindows()