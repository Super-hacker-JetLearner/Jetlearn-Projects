import cv2
import numpy as np
import os

folder_path = '/Users/s932172@aics.espritscholen.nl/Desktop/game development/cv development'

os.chdir(folder_path)

recycle_image = cv2.imread('recycle background.png')

cv2.imshow('cv2 development', recycle_image)

# cv2.waitKey(0)

print(recycle_image)

kernel = np.ones((9, 9), np.uint8)
eroded_image = cv2.erode(recycle_image, kernel)

cv2.imshow('eroded image', eroded_image)


blurred_image0 = cv2.GaussianBlur(recycle_image, (9,9), 0)
cv2.imshow('gaussian blur 0', blurred_image0)

blurred_image1 = cv2.GaussianBlur(recycle_image, (9,9), 15)
cv2.imshow('gaussian blur 1', blurred_image1)

median_blur = cv2.medianBlur(recycle_image, 9)
cv2.imshow('median blur', median_blur)

bilateral_filter = cv2.bilateralFilter(recycle_image, 9, 70, 70)
cv2.imshow('bilateral filter', bilateral_filter)


bordered_image = cv2.copyMakeBorder(recycle_image, 50, 50, 50, 50, cv2.BORDER_CONSTANT, value=[255, 255, 255])
cv2.imshow('bordered image', bordered_image)

reflected_border = cv2.copyMakeBorder(recycle_image, 100, 100, 100, 100, cv2.BORDER_REFLECT)
cv2.imshow('reflected border image', reflected_border)


cv2.waitKey(0)
cv2.destroyAllWindows()