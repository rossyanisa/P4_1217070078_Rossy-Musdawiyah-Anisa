# Rossy Musdawiyah Anisa, 1217070078

import cv2
import numpy as np
image = cv2.imread("kucing.jpg")
b,g,r = cv2.split(image)
#buat matriks seukuran dengan citra
matriks0 = np.zeros(image.shape[:2],image.dtype)
m = matriks0
#merge matriks dengan matriks citra merah
merah = cv2.merge([m,m,r])
cv2.imshow('Citra red channel', merah)
cv2.waitKey(0)