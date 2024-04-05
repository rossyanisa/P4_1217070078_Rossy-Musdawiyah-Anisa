# Rossy Musdawiyah Anisa, 1217070078

import cv2
import numpy as np

image = cv2.imread('kucing.jpg')
height, width = image.shape[:2]

#membuat matriks M dengan contoh Tx = 100 & Ty=50
M = np.float32([[1,0,100], [0,1,50]])
image_translation = cv2.warpAffine (image, M, (height, width))
cv2.imshow('Citra', image) 
cv2.imshow('Citra Hasil Translasi', image_translation)
cv2.waitKey(0)