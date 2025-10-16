import cv2
import os
import numpy as np


folder_path = '/Users/s932172@aics.espritscholen.nl/Desktop/game development/cv development'

os.chdir(folder_path)

landscape = cv2.imread('landscape.webp')

# cv2.imshow('landscape', landscape)


# start_point = (100, 200)
# end_point = (500, 400)
color = [0, 255, 255]
thickness = 10

# line_image = cv2.line(landscape, start_point, end_point, color, thickness)
line_image = cv2.line(landscape, (0, 50), (150, 100), color, thickness)
line_image = cv2.line(landscape, (0, 50), (200, 50), color, thickness)
line_image = cv2.line(landscape, (50, 0), (150, 100), color, thickness)
line_image = cv2.line(landscape, (50, 0), (0, 100), color, thickness)
line_image = cv2.line(landscape, (0, 100), (200, 50), color, thickness)

cv2.imshow('line image', line_image)


cv2.waitKey(0)
cv2.destroyAllWindows()