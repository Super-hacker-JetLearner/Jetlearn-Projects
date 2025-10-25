import cv2
import os
import numpy as np


folder_path = '/Users/s932172@aics.espritscholen.nl/Desktop/game development/cv development'
os.chdir(folder_path)

video = cv2.VideoCapture('invisibility_video.mov')


bg_frames = []
num_bg_frames = 50

for i in range(num_bg_frames):
    ret, frame = video.read()
    if not ret:
        print('Frame could not be read')
        continue
    bg_frames.append(frame)

if len(bg_frames) == 0:
    print("No background")
    exit()

background = np.median(bg_frames, axis=0).astype(np.uint8)
background = np.flip(background, axis=1)

green_low = np.array([30, 30, 15])
green_top = np.array([100, 255, 200])

kernel = np.ones((7, 7), np.uint8)


while video.isOpened():
    # frame_is, frame = video.read()
    # if not frame_is:
    #     break

    # frame = np.flip(frame, axis=1)
    # frame = cv2.GaussianBlur(frame, (3, 3), 0)
    # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # mask = cv2.inRange(hsv, green_low, green_top)

    # mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
    # mask = cv2.medianBlur(mask, 7)
    # mask = cv2.GaussianBlur(mask, (7,7), 0)
    
    # mask_inv = cv2.bitwise_not(mask)
    
    # cloak_area = cv2.bitwise_and(background, background, mask=mask)
    # not_cloak_area = cv2.bitwise_and(frame, frame, mask=mask_inv)

    
    
        
    # final_frame = cv2.addWeighted(cloak_area, 1, not_cloak_area, 1, 0)
    
    
    
    

    # cv2.imshow('invisibility cloak', final_frame)

    # key = cv2.waitKey(5)
    # if key == 27:
    #     break
    
    
    is_frame, frame = video.read()
    if not is_frame:
        print('cannot read frame to flip')
        break
    frame = np.flip(frame, axis=1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    final_mask = cv2.inRange(hsv, green_low, green_top)
    final_mask = cv2.morphologyEx(final_mask, cv2.MORPH_OPEN, kernel, iterations=1)
    
    inverted = cv2.bitwise_not(final_mask)
    
    red_colors = cv2.bitwise_and(background, background, mask=final_mask)
    not_red_colors = cv2.bitwise_and(frame, frame, mask=inverted)
    
    final_frame = cv2.addWeighted(red_colors, 1, not_red_colors, 1, 0)
    cv2.imshow('invisible image', final_frame)
    x = cv2.waitKey(5)
    if x == 27:
        break


video.release()
cv2.destroyAllWindows()
