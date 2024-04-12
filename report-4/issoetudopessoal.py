import cv2
import numpy as np

img = cv2.imread('issoetudopessoal.jpg')

h, w, _ = img.shape

out = cv2.VideoWriter('issoetudopessoal.avi', cv2.VideoWriter_fourcc(*'XVID'), 24, (w, h))

r = int(np.sqrt(np.power(h / 2, 2) + np.power(w / 2, 2)))

s = 10

black_img = np.zeros_like(img)

while r > 0:
    new_image = black_img.copy()
    
    cv2.circle(new_image, (int(w/2), int(h/2)), r, (255, 255, 255), thickness=-1)
    
    new_image = cv2.bitwise_and(img, new_image)
    
    out.write(new_image)
    
    cv2.imshow('Isso eh tudo pepepessoal', new_image)
    
    r -= s
    
    if r <= 0:
        break

    cv2.waitKey(50)

out.release()
cv2.destroyAllWindows()
