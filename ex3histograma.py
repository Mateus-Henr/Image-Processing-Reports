import cv2
import numpy as np

gray_img = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Imagem cinza', gray_img)
img = cv2.imread('lena.jpg')
cv2.imshow('Imagem colorida', img)

gray_hist = cv2.calcHist([gray_img], [0], None, [256], [0, 256], accumulate=False)
gray_hist_img = np.zeros((400, 512), dtype=np.uint8)
cv2.normalize(gray_hist, gray_hist, alpha=0, beta=400, norm_type=cv2.NORM_MINMAX)
for i in range(1, 256):
      cv2.line(gray_hist_img, (2*(i-1), 400 - int((gray_hist[i-1]))),
              (2*(i), 400 - int((gray_hist[i]))),
              (255, 0, 0), thickness=2)

cv2.imshow('Histograma cinza', gray_hist_img)

b_hist = cv2.calcHist([img], [0], None, [256], [0, 256], accumulate=False)
g_hist = cv2.calcHist([img], [1], None, [256], [0, 256], accumulate=False)
r_hist = cv2.calcHist([img], [2], None, [256], [0, 256], accumulate=False)
hist_img = np.zeros((400, 512, 3), dtype=np.uint8)

cv2.normalize(b_hist, b_hist, alpha=0, beta=400, norm_type=cv2.NORM_MINMAX)
cv2.normalize(g_hist, g_hist, alpha=0, beta=400, norm_type=cv2.NORM_MINMAX)
cv2.normalize(r_hist, r_hist, alpha=0, beta=400, norm_type=cv2.NORM_MINMAX)

for i in range(1, 256):
      cv2.line(hist_img, (2*(i-1), 400 - int((b_hist[i-1]))),
              (2*(i), 400 - int((b_hist[i]))),
              (255, 0, 0), thickness=2)
      cv2.line(hist_img, (2*(i-1), 400 - int((g_hist[i-1]))),
              (2*(i), 400 - int((g_hist[i])) ),
              (0, 255, 0), thickness=2)
      cv2.line(hist_img, (2*(i-1), 400 - int((r_hist[i-1]))),
              (2*(i), 400 - int((r_hist[i]))),
              (0, 0, 255), thickness=2)

cv2.imshow('Histograma colorido', hist_img)

while True:
    k = cv2.waitKey(0) & 0xFF     
    if k == 27: break             # ESC key to exit 
cv2.destroyAllWindows()