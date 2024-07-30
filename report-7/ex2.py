import cv2
import numpy as np

def process_image(filename):
    #input de imagem
    img = cv2.imread(filename)
    img = cv2.GaussianBlur(img, (5, 5), 0)

    # Converte pra escala cinza
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detecção de bordas
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    # Aplicação da transformada de Hough
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)

    # Cria uma copia da imagem original
    line_img = np.copy(img)

    # Desenha as linhas da imagem
    if lines is not None:
        for rho, theta in lines[:, 0]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))

            # Filtra linhas de acordo com orientação
            if abs(theta) < np.pi / 4 or abs(theta) > 3 * np.pi / 4:  # Vertical
                cv2.line(line_img, (x1, y1), (x2, y2), (0, 0, 255), 2)
            elif abs(theta - np.pi / 2) < np.pi / 4:  # Horizontal
                cv2.line(line_img, (x1, y1), (x2, y2), (0, 0, 255), 2)

    # Display
    cv2.imshow(f'Detected Lines - {filename}', line_img)
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()

process_image('camisa1.jpg')
process_image('camisa2.png')