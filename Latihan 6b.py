# Rossy Musdawiyah Anisa, 1217070078

import cv2
import numpy as np

image = cv2.imread('kucing.jpg')

#untuk mengetahui ukuran citra lebar dan tinggi
(height, width) = image.shape[0:2]
RotasiMatriks = cv2.getRotationMatrix2D((width/2, height/2),-90,0.5)

#rotasi dapat menggunakan method wrapAffine mengambil citra asli
RotasiCitra = cv2.warpAffine (image, RotasiMatriks, (width, height))
cv2.imshow('Citra Rotasi', RotasiCitra)
cv2.waitKey(0)