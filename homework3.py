import cv2
import os
import numpy as np


folder_path = '/Users/s932172@aics.espritscholen.nl/Desktop/game development/cv development'

os.chdir(folder_path)

# image = np.zeros((1000, 1000, 3), dtype=np.uint8)
# cv2.imshow('black background', image)
image = cv2.imread('people2.png')

# radius = 100
# color = (0, 255, 255)

# image =cv2.circle(image, (300, 300), radius, color, thickness=-1)
# image =cv2.circle(image, (500, 500), radius, (255, 0, 0), thickness=-1)
# image =cv2.circle(image, (650, 650), radius, (0, 255, 0), thickness=-1)
# image =cv2.circle(image, (150, 150), radius, (255, 255, 255), thickness=-1)
# image =cv2.circle(image, (800, 800), radius, (255, 255, 255), thickness=-1)

# circle_image =cv2.circle(image, (300, 300), radius, color, thickness=-1)


image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image = cv2.GaussianBlur(image, (9, 9), 0)

cv2.imshow('circle image', image)



parameters = cv2.SimpleBlobDetector_Params()
parameters.filterByArea = True
parameters.minArea = 100
parameters.maxArea = 100000
# parameters.filterByCircularity = False
# parameters.minCircularity = 0.00000000000000000001
# parameters.filterByConvexity = False
# parameters.minConvexity = 0.0000000000000000000001
# parameters.filterByInertia = False
# parameters.minInertiaRatio = 0.00000000000000000001
# parameters.filterByColor = True
# parameters.blobColor = 0

# edges = cv2.Canny(image, 50, 50)
# cv2.imshow('edges', edges)

# version = cv2.__version__.split('.')
# print(version)
# if int(version[0]) < 3:
#     detector = cv2.SimpleBlobDetector(parameters)
# else:
#     detector = cv2.SimpleBlobDetector_create(parameters)

detector = cv2.SimpleBlobDetector_create(parameters)


key_points = detector.detect(image)
blobs = cv2.drawKeypoints(image, key_points, image, (255, 100, 100), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
number = len(key_points)
print(number)
cv2.imshow('detected', blobs)



cv2.waitKey(0)
cv2.destroyAllWindows()