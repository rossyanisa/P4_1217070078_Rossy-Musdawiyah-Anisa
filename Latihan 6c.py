# Rossy Musdawiyah Anisa, 1217070078

#proses operasi flipping citra

import cv2
import numpy as np

image = cv2.imread('kucing.jpg')

#flipping horizontal
flip_hor=cv2.flip(image, 1)

#flipping vertical
flip_ver=cv2.flip(image,0)

#flipping vertical-horizontal
flip_verhor=cv2.flip(image,-1)
cv2.imshow('Citra', image)
cv2.imshow('Citra Flip Horizontal', flip_hor)
cv2.imshow('Citra Flip Vertical', flip_ver)
cv2.imshow('Citra Flip Vertical-Horizontal', flip_verhor)
cv2.waitKey(0)