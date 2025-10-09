import cv2
import os
import numpy as np


folder_path = '/Users/s932172@aics.espritscholen.nl/Desktop/game development/cv development'

os.chdir(folder_path)

landscape = cv2.imread('landscape.webp')

cv2.imshow('landscape', landscape)


resized = cv2.resize(landscape, (600, 300))
cv2.imshow('resized', resized)


gaussian_blur = cv2.GaussianBlur(landscape, (9, 9), 0)
cv2.imshow('gaussian blur', gaussian_blur)

kernel = np.ones((9, 9), np.uint8)
eroded = cv2.erode(landscape, kernel)
cv2.imshow('eroded', eroded)


median_blur = cv2.medianBlur(landscape, 7)
cv2.imshow('median blur', median_blur)

bilateral_filter = cv2.bilateralFilter(landscape, 7, 60, 60)
cv2.imshow('bilateral filter', bilateral_filter)


bordered_image = cv2.copyMakeBorder(landscape, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=[255, 255, 255])
cv2.imshow('bordered image', bordered_image)

reflected_border = cv2.copyMakeBorder(landscape, 70, 70, 70, 70, cv2.BORDER_REFLECT)
cv2.imshow('reflected border image', reflected_border)

blur = cv2.blur(landscape, (9,9))
cv2.imshow('blur', blur)

stack_blur = cv2.stackBlur(landscape, (3,3))
cv2.imshow('stack blur', stack_blur)


cv2.waitKey(0)
cv2.destroyAllWindows()