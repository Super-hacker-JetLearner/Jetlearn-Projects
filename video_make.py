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
        
        
images.sort()

# mean_width = 0
# mean_height = 0


# for image in images:
#     img = Image.open(os.path.join(path, image))
#     width, height = img.size
#     mean_width += width
#     mean_height += height
    
    
# mean_width/= len(images)
# mean_height/= len(images)

# mean_height = int(mean_height)
# mean_width = int(mean_width)

# for image in images:
#     img = Image.open(os.path.join(path, image))
#     im_resized = img.resize((mean_width, mean_height))
#     im_resized.save(image, 'JPEG', quality=95)
    

def generate_video():
    image_folder = path
    video_name = 'mygeneratedvideo.mp4'
    output_folder = '/Users/s932172@aics.espritscholen.nl/Desktop/game development/cv development'
    video_path = os.path.join(output_folder, video_name)
    
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc(*'mp4v'), 0.5, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))


    video.release()
    
    
generate_video()