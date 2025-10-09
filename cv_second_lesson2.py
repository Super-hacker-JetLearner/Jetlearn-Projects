import cv2
import os
import numpy as np


folder_path = '/Users/s932172@aics.espritscholen.nl/Desktop/game development/cv development'

os.chdir(folder_path)

recycle_image = cv2.imread('recycle background.png')
# recycle_image = cv2.resize(recycle_image, (200, 200))

white_image = cv2.imread('white image2.png')

cv2.imshow('cv2 development', recycle_image)

cv2.imshow('white image', white_image)

grayscale = cv2.cvtColor(recycle_image, cv2.COLOR_BGR2GRAY)
cv2.imshow('grayscale image', grayscale)

        
        
# def make_grayscale(image:cv2.typing.MatLike):
#     new_image = image.copy()
#     rows, columns = new_image.shape[0:2]
#     for row in range(rows):
#         for col in range(columns):
#             result = sum(new_image[row][col])
#             # if result > 255:
#             #     result = 255
#             new_image[row][col] = result
            
#     return new_image

def make_grayscale(image: cv2.typing.MatLike):
    rows, columns = image.shape[:2]
    gray_image = np.zeros((rows, columns), dtype=np.uint8)
    for row in range(rows):
        for col in range(columns):
            b, g, r = image[row][col]
            gray_image[row][col] = int(0.114 * b + 0.587 * g + 0.299 * r)

    return gray_image



grayscale_white_self = make_grayscale(white_image)
cv2.imshow('white image grayscale self', grayscale_white_self)

grayscale_recycle_self = make_grayscale(recycle_image)
cv2.imshow('recycle image grayscale self', grayscale_recycle_self)

cv2.waitKey(0)
cv2.destroyAllWindows()