import cv2
import os
import numpy as np


folder_path = '/Users/s932172@aics.espritscholen.nl/Desktop/game development/cv development'

os.chdir(folder_path)

circles = cv2.imread('yellow_image.png')
cv2.imshow('circles', circles)

parameters = cv2.SimpleBlobDetector_Params()
parameters.filterByArea = True
parameters.minArea = 1000
parameters.filterByCircularity = True
parameters.minCircularity = 0.00000000000000000001
parameters.filterByConvexity = True
parameters.minConvexity = 0.0000000000000000000001
parameters.filterByInertia = True
parameters.minInertiaRatio = 0.00000000000000000001
parameters.filterByColor = False
parameters.blobColor = 0


edge_detection = cv2.Canny(circles, 100, 200)
cv2.imshow('edge detection', edge_detection)

detector = cv2.SimpleBlobDetector_create(parameters)
key_points = detector.detect(edge_detection)

blobs = cv2.drawKeypoints(circles, key_points, circles, [255, 100, 100], cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
number = len(key_points)
print(number)
cv2.imshow('detected', blobs)



cv2.waitKey(0)
cv2.destroyAllWindows()