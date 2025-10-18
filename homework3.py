import cv2
import os
import numpy as np


folder_path = '/Users/s932172@aics.espritscholen.nl/Desktop/game development/cv development'

os.chdir(folder_path)

image = cv2.imread('black.png')
cv2.imshow('black background', image)

radius = 100
color = [0, 255, 255]

image =cv2.circle(image, (300, 300), radius, color, thickness=-1)
image =cv2.circle(image, (500, 500), radius, [255, 0, 0], thickness=-1)
image =cv2.circle(image, (650, 650), radius, [0, 255, 0], thickness=-1)
image =cv2.circle(image, (150, 150), radius, [0, 0, 255], thickness=-1)
# circle_image =cv2.circle(image, (300, 300), radius, color, thickness=-1)

cv2.imshow('circle image', image)



parameters = cv2.SimpleBlobDetector_Params()
# parameters.filterByArea = True
# parameters.minArea = 100
parameters.filterByCircularity = True
parameters.minCircularity = 0.00000000000000000001
parameters.filterByConvexity = True
parameters.minConvexity = 0.0000000000000000000001
parameters.filterByInertia = True
parameters.minInertiaRatio = 0.00000000000000000001
parameters.filterByColor = True
parameters.blobColor = 255


detector = cv2.SimpleBlobDetector_create(parameters)
key_points = detector.detect(image)
print(key_points)
blobs = cv2.drawKeypoints(image, key_points, image, [255, 100, 100], cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
number = len(key_points)
print(number)
cv2.imshow('detected', blobs)



cv2.waitKey(0)
cv2.destroyAllWindows()