import cv2
import random

# ORIGINAL IMAGE
image = cv2.imread('image.jpeg')
cv2.imshow('image', image)
cv2.waitKey(0) # Maintain output window until user presses a key
cv2.destroyAllWindows() # Destroying present windows on screen

# RESIZING
size = 128
res = cv2.resize(image, dsize = (size, size), interpolation = cv2.INTER_CUBIC)
cv2.imshow('image', res)
cv2.waitKey(0) # Maintain output window until user presses a key
cv2.destroyAllWindows() # Destroying present windows on screen

# MASK 64x64 @ random location
mask_size = 48

x_rand = random.randrange(0, size-mask_size-1)
y_rand = random.randrange(0, size-mask_size-1)

for i in range(x_rand, x_rand+mask_size-1):
    for j in range(y_rand, y_rand+mask_size-1):
        # pixel rgb values for the mask
        rgb_mask = [[48,48,48],[64,64,64],[80,80,80],[96,96,96],[128,128,128],
               [255,153,104],[0,0,102],[153,255,204],[153,255,51],[255,255,102]]
        random_index = random.randrange(0, 9)
        res[i][j] = rgb_mask[random_index]

cv2.imshow('image', res)
cv2.waitKey(0) # Maintain output window until user presses a key
cv2.destroyAllWindows() # Destroying present windows on screen