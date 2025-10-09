import cv2
import os
import numpy as np


folder_path = '/Users/s932172@aics.espritscholen.nl/Desktop/game development/cv development'

os.chdir(folder_path)

circles = cv2.imread('circles.jpg')
cv2.imshow('circles', circles)

grayscale = cv2.cvtColor(circles, cv2.COLOR_BGR2GRAY)

blurred = cv2.blur(grayscale, (3,3))
cv2.imshow('blurred', blurred)

detected = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, 100, param1=50, param2=50, minRadius=10, maxRadius=300)
detected = np.round(detected)
detected = np.uint16(detected)

color = [200, 0, 0]
thickness = 10

print(detected)

for circle in detected[0, :]:
    x, y, radius = circle
    cv2.circle(circles, (x,y), radius, color, thickness)
    
cv2.imshow('detected', circles)

cv2.waitKey(0)
cv2.destroyAllWindows()
