import cv2
import os
import numpy as np


folder_path = '/Users/s932172@aics.espritscholen.nl/Desktop/game development/cv development'

os.chdir(folder_path)

landscape = cv2.imread('landscape.webp')

cv2.imshow('landscape', landscape)

rotate = np.rot90(landscape)
cv2.imshow('rotate', rotate)

width, height = landscape.shape[:2]
rotated_matrix = cv2.getRotationMatrix2D((width/2, height/2), 45, 1)



rotated_image = cv2.warpAffine(landscape, rotated_matrix, (width, height))
cv2.imshow('rotated image', rotated_image)

edge_detection = cv2.Canny(landscape, 100, 200)
cv2.imshow('edge detection', edge_detection)


hsv = cv2.cvtColor(landscape, cv2.COLOR_BGR2HSV)
cv2.imshow('hsv', hsv)

start_point = (100, 200)
end_point = (500, 400)
color = [0, 0, 255]
thickness = 10

line_image = cv2.line(landscape, start_point, end_point, color, thickness)
cv2.imshow('line image', line_image)

topleft = (100, 100)
bottomright = (500, 600)
color = [0, 255, 0]

rect_image = cv2.rectangle(landscape, topleft, bottomright, color, thickness=-1)
cv2.imshow('rect image', rect_image)

center = (300, 300)
radius = 200
color = [255, 0, 0]

circle_image =cv2.circle(landscape, center, radius, color, thickness=-1)
cv2.imshow('circle image', circle_image)


font = cv2.FONT_ITALIC
text = 'hello'
location = (500, 300)
color = [255, 255, 0]
thickness = 2
size = 2
text_image = cv2.putText(landscape, text, location, font, size, color, thickness, cv2.LINE_AA)
cv2.imshow('text image', text_image)





cv2.waitKey(0)
cv2.destroyAllWindows()