import cv2
import numpy as np

path = 'camisa1.jpg'
img = cv2.imread(path)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# edges = cv2.Canny(gray_img, 500, 600)

# circulos = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1.2, minDist=10,
#                            param1=100, param2=12, minRadius=5, maxRadius=10)

# botoes = 0
# abotoados = 0
# if circulos is not None:
#     circulos = np.round(circulos[0, :]).astype("int")
#     botoes = len(circulos)

#     x_pos = [x for x, y, r in circulos]
#     x_pos.sort()
    
#     for i in range(len(x_pos)):
#         n = 0
#         for j in range(len(x_pos)):
#             if i != j and abs(x_pos[i] - x_pos[j]) <= 10:
#                 n += 1
#         if n >= 2:
#             abotoados += 1
#     print(x_pos)

#     for (x, y, r) in circulos:
#         cv2.circle(img, (x, y), r, (0, 255, 0), 4)
#         cv2.rectangle(img, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

edges = cv2.Canny(gray_img, 60, 120)

linhas = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=120, minLineLength=70, maxLineGap=10)

if linhas is not None:
    for linha in linhas:
        for x1, y1, x2, y2 in linha:
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 2)

cv2.imwrite('camisa1linhas.png', img)
print(f"Número de botões: {botoes}\nNúmero de botões abotoados: {abotoados}")