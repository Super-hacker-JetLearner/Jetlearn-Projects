import cv2
import os


folder_path = '/Users/s932172@aics.espritscholen.nl/Desktop/game development/cv development'

os.chdir(folder_path)

recycle_image = cv2.imread('recycle background.png')
# recycle_image = cv2.resize(recycle_image, (200, 200))

white_image = cv2.imread('white image2.png')

cv2.imshow('cv2 development', recycle_image)

cv2.imshow('white image', white_image)

grayscale = cv2.cvtColor(recycle_image, cv2.COLOR_BGR2GRAY)
cv2.imshow('grayscale image', grayscale)

rows, columns = recycle_image.shape[0:2]
print(recycle_image.shape)
for row in range(rows):
    for col in range(columns):
        result = sum(recycle_image[row][col])
        if result > 255:
            result = 255
        recycle_image[row][col] = result
        

print(white_image[50][50])


rows, columns = white_image.shape[0:2]
for row in range(rows):
    for col in range(columns):
        result = sum(white_image[row][col])
        if result > 255:
            result = 255
        white_image[row][col] = result
        

cv2.imshow('grayscale white', white_image)
cv2.imshow('grayscale recycle self', recycle_image)

cv2.waitKey(0)
cv2.destroyAllWindows()