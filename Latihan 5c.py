# Rossy Musdawiyah Anisa, 1217070078

import cv2
import numpy as np

# membuat matriks untuk menggambar persegi 
persegi = np.zeros((400,400), dtype="uint8")

#sintaks method rectangle (var, (titik awal), (lebar, tinggi), warna, thickness)
# jika thickness diisi 1 maka objek akan diisi warna penuh
cv2.rectangle(persegi, (60,60), (340,340), 255,-1) 

#membuat matriks untuk menggambar lingkaran
lingkaran = np.zeros((400,400), dtype="uint8")

#sintaks method circle (var, (titik pusat), radius (r)/jari-jari, warna, thickness)
cv2.circle(lingkaran, (200, 200),150,255,-1)

# Penggunaan operator xor
operasiXOR = cv2.bitwise_xor(persegi, lingkaran)

cv2.imshow("Persegi", persegi)
cv2.imshow("Lingkaran", lingkaran)
cv2.imshow("Operasi Xor", operasiXOR)
cv2.waitKey(0)