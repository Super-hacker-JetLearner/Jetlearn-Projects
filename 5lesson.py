import cv2
import os
import PIL
import numpy as np


folder_path = '/Users/s932172@aics.espritscholen.nl/Desktop/game development/cv development'

os.chdir(folder_path)


video = cv2.VideoCapture('person_video.mp4')


background = None



for i in range(50):
    is_frame, frame = video.read()
    if not is_frame:
        print('not able to read frames')
        continue
    background = frame
    

if background is None:
    print('no background')
    
    
# video.release()


background = np.flip(background, axis=1)
# background = cv2.cvtColor(background, cv2.COLOR_BGR2HSV)


while video.isOpened():
    is_frame, frame = video.read()
    if not is_frame:
        print('cannot read frame to flip')
        break
    frame = np.flip(frame, axis=1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, 0, 38])
    upper_red = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    lower_red2 = np.array([158, 0, 30])
    upper_red2 = np.array([179, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    final_mask = mask1 + mask2
    kernel = np.ones((3, 3), np.uint8)
    final_mask = cv2.morphologyEx(final_mask, cv2.MORPH_OPEN, kernel, iterations=1)
    
    inverted = cv2.bitwise_not(final_mask)
    
    red_colors = cv2.bitwise_and(background, background, mask=final_mask)
    not_red_colors = cv2.bitwise_and(frame, frame, mask=inverted)
    
    final_frame = cv2.addWeighted(red_colors, 1, not_red_colors, 1, 0)
    cv2.imshow('invisible image', final_frame)
    x = cv2.waitKey(5)
    if x == 27:
        break
    
    
    
    
# cv2.waitKey(0)
cv2.destroyAllWindows()