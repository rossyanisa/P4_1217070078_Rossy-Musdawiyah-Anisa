# Rossy Musdawiyah Anisa, 1217070078

import cv2
import numpy as np

image = cv2.imread('kucing.jpg')

#maksimum pixel
max_pixel_value = 255
#rumus citra negatif 255 - f(x,y)
inverted_image = max_pixel_value - image

cv2.imshow('Original Image', image)
cv2.imshow('Citra negatif', inverted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()