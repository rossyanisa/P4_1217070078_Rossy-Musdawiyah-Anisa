# Rossy Musdawiyah Anisa, 1217070078

import cv2

image = cv2.imread('kucing.jpg')

# Faktor skalla
zoom_factor = 1.5 # penambaahn untuk zoom in

# mendapatkan dimensi gambar
height, width = image.shape[:2]

# hitung dimensi baru
new_height = int(height * zoom_factor)
new_width = int(width* zoom_factor)

# Resize gambar
scaled_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

cv2.imshow('Original Image', image)
cv2.imshow('Image Zooming', scaled_image)
cv2.waitKey(0)
cv2.destroyAllWindows()