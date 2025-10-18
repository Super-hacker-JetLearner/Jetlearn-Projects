import cv2
import numpy as np
from PIL import Image
import os


path = '/Users/s932172@aics.espritscholen.nl/Desktop/game development/cv development/images_for_video'
os.chdir(path)

images = []
for image in os.listdir('.'):
    if image.endswith(('.png', '.jpg', '.jpeg')):
        images.append(image)
        
        
mean_width = 0
mean_height = 0

for image in images:
    img = Image.open(os.path.join(path, image))
    width, height = img.size
    mean_width += width
    mean_height += height
    
    
mean_width/= len(images)
mean_height/= len(images)

