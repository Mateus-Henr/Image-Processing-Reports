import cv2
import numpy as np
from matplotlib import pyplot as plt

gray_img = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Imagem cinza', gray_img)
hist = cv2.calcHist([gray_img], [0], None, [256], [0, 256])
plt.hist(gray_img.ravel(), 256, [0,256])
plt.show()

img = cv2.imread('lena.jpg')
cv2.imshow('Imagem', img)
bhist = cv2.calcHist([img], [0], None, [256], [0, 256], accumulate=False)
ghist = cv2.calcHist([img], [1], None, [256], [0, 256], accumulate=False)
rhist = cv2.calcHist([img], [2], None, [256], [0, 256], accumulate=False)
plt.hist(img.ravel(), 256, [0,256])
plt.show()

while True:
    k = cv2.waitKey(0) & 0xFF     
    if k == 27: break             # ESC key to exit 
cv2.destroyAllWindows()