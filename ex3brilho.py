import cv2
import numpy as np

def histograma(img, name):
    bgr_planes = cv2.split(img)

    b_hist = cv2.calcHist(bgr_planes, [0], None, [256], [0, 256], accumulate=False)
    g_hist = cv2.calcHist(bgr_planes, [1], None, [256], [0, 256], accumulate=False)
    r_hist = cv2.calcHist(bgr_planes, [2], None, [256], [0, 256], accumulate=False)
    hist_img = np.zeros((400, 512, 3), dtype=np.uint8)

    cv2.normalize(b_hist, b_hist, alpha=0, beta=400, norm_type=cv2.NORM_MINMAX)
    cv2.normalize(g_hist, g_hist, alpha=0, beta=400, norm_type=cv2.NORM_MINMAX)
    cv2.normalize(r_hist, r_hist, alpha=0, beta=400, norm_type=cv2.NORM_MINMAX)

    for i in range(1, 256):
        cv2.line(hist_img, (2*(i-1), 400 - int(b_hist[i-1])),
                (2*(i), 400 - int(b_hist[i])),
                (255, 0, 0), thickness=2)
        cv2.line(hist_img, (2*(i-1), 400 - int(g_hist[i-1])),
                (2*(i), 400 - int(g_hist[i])),
                (0, 255, 0), thickness=2)
        cv2.line(hist_img, (2*(i-1), 400 - int(r_hist[i-1])),
                (2*(i), 400 - int(r_hist[i])),
                (0, 0, 255), thickness=2)
    
    cv2.imshow(name, hist_img)

def controller(img, brilho = 255):
    brilho = int((brilho - 0) * (255 - (-255)) / (510 - 0) + (-255))
    if brilho != 0:
        if brilho > 0:
             shadow = brilho
             max = 255
        else:
            shadow = 0
            max = 255 + brilho
        al_pha = (max - shadow) / 255
        ga_mma = shadow

        cal = cv2.addWeighted(img, al_pha, img, 0, ga_mma)
 
    else:
        cal = img

    return cal

def mudarBrilho(brilho = 0):
    brilho = cv2.getTrackbarPos('Brilho', 'Mudança de brilho')
    effect = controller(img, brilho)

    cv2.imshow('Mudança de brilho', effect)
    histograma(effect, 'Histograma modificado')


img = cv2.imread('lena.jpg')

cv2.namedWindow('Mudança de brilho')

cv2.imshow('Mudança de brilho', img)

cv2.createTrackbar('Brilho', 'Mudança de brilho', 255, 2 * 255, mudarBrilho)
      
mudarBrilho(0)

cv2.waitKey(0)
cv2.destroyAllWindows()