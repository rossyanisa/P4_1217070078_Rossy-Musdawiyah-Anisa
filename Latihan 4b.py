# Rossy Musdawiyah Anisa, 12170700078

import cv2

# Membaca dua gambar
gambar1 = cv2.imread('kucing.jpg')
gambar2 = cv2.imread('astro.jpg')

#Pastikan kedua gambar memiliki dimensi yang sama 
tinggi, lebar, _ = gambar1.shape
gambar2 = cv2.resize(gambar2, (lebar, tinggi))

# Membuat gambar hasil penjumlahan 
hasil_penjumlahan = gambar1.copy()

# Melakukan penjumlahan manual untuk setiap piksel
for y in range(tinggi):
    for x in range(lebar): 
        for c in range(3): # Loop untuk masing-masing channel (BGR) 
            nilai_baru = int(gambar1[y, x, c]) + int(gambar2[y, x, c]) 
            hasil_penjumlahan[y, x, c] = min(nilai_baru, 255) # Batasi nilai maksimal menjadi 255

# Menampilkan dan menyimpan gambar hasil penjumlahan 
cv2.imshow('Hasil Penjumlahan', hasil_penjumlahan) 
cv2.waitKey(0) 
cv2.destroyAllWindows()

# Opsional: Menyimpan hasil penjumlahan 
cv2.imwrite('hasil_penjumlahan_manual_rumus.jpg', hasil_penjumlahan)
