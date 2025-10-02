import cv2
import os



folder_path = '/Users/s932172@aics.espritscholen.nl/Desktop/game development/cv development'

os.chdir(folder_path)

# image = cv2.imread('/Users/s932172@aics.espritscholen.nl/Desktop/game development/cv development/grass.png', cv2.IMREAD_COLOR)
# image_grayscale = cv2.imread('/Users/s932172@aics.espritscholen.nl/Desktop/game development/cv development/grass.png', cv2.IMREAD_GRAYSCALE)

recyle_image = cv2.imread('recycle background.png')
alien_image = cv2.imread('alien.png')


# cv2.imwrite('new_image.png', image)

# cv2.imshow('grass image', image)

# cv2.imshow('grass image grayscale', image_grayscale)

cv2.imshow('recycle image', recyle_image)
b, g, r = cv2.split(recyle_image)

cv2.imshow('recycle image b', b)
cv2.imshow('recycle image g', g)
cv2.imshow('recycle image r', r)

cv2.imshow('alien image', alien_image)
b, g, r = cv2.split(alien_image)

cv2.imshow('alien image b', b)
cv2.imshow('alien image g', g)
cv2.imshow('alien image r', r)





cv2.waitKey(0)

cv2.destroyAllWindows()