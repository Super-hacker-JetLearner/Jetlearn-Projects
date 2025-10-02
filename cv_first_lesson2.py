import cv2
import os

folder_path = '/Users/s932172@aics.espritscholen.nl/Desktop/game development/cv development'

os.chdir(folder_path)

# image = cv2.imread('/Users/s932172@aics.espritscholen.nl/Desktop/game development/cv development/grass.png', cv2.IMREAD_COLOR)
# image_grayscale = cv2.imread('/Users/s932172@aics.espritscholen.nl/Desktop/game development/cv development/grass.png', cv2.IMREAD_GRAYSCALE)

recyle_image = cv2.imread('recycle background.png')
alien_image = cv2.imread('alien.png')


resized_recycle_image = cv2.resize(recyle_image, (500, 400))
resized_alien_image = cv2.resize(alien_image, (500, 400))

title = 'image'


cv2.imshow(title, recyle_image)
cv2.waitKey(0)

cv2.imshow(title, resized_recycle_image)
cv2.waitKey(0)

cv2.imshow(title, alien_image)
cv2.waitKey(0)

cv2.imshow(title, resized_alien_image)
cv2.waitKey(0)


weighted_image = cv2.addWeighted(resized_recycle_image, 0.5, resized_alien_image, 0.5, 0)
cv2.imshow(title, weighted_image)
cv2.waitKey(0)

weighted_image2 = cv2.addWeighted(resized_recycle_image, 0.7, resized_alien_image, 0.3, 0)
cv2.imshow(title, weighted_image2)
cv2.waitKey(0)

weighted_image3 = cv2.addWeighted(resized_recycle_image, 0.3, resized_alien_image, 0.7, 0)
cv2.imshow(title, weighted_image3)
cv2.waitKey(0)

subtracted_image = cv2.subtract(resized_recycle_image, resized_alien_image)
cv2.imshow(title, subtracted_image)
cv2.waitKey(0)


cv2.destroyAllWindows()