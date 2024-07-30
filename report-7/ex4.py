import cv2
import numpy as np

# Função para calcular a distância entre dois pontos
def euclidean_distance(p1, p2):
    return np.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# Função de callback para registrar os pontos clicados na imagem original
def click_points(event, x, y, flags, param):
    global points
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        cv2.circle(image, (x, y), 5, (0, 255, 0), -1)
        cv2.imshow("Image", image)

# Função de callback para registrar os pontos de referência na imagem original
def click_reference_points_original(event, x, y, flags, param):
    global ref_points_original
    if event == cv2.EVENT_LBUTTONDOWN:
        ref_points_original.append((x, y))
        cv2.circle(image, (x, y), 5, (0, 255, 0), -1)
        cv2.imshow("Image", image)

# Carregar e redimensionar a imagem
image_path = 'quadratenis2.png'
image = cv2.imread(image_path)
height, width = image.shape[:2]
new_width = 800
aspect_ratio = new_width / float(width)
new_height = int(height * aspect_ratio)
image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)

orig = image.copy()
cv2.imshow("Image", image)

# Captura os 4 pontos para a transformação de perspectiva
points = []
cv2.namedWindow("Image")
cv2.setMouseCallback("Image", click_points)

print("Clique nos 4 pontos que definem a área da quadra (cantos da quadra):")

while True:
    cv2.imshow("Image", image)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # Pressione 'Esc' para sair sem selecionar os pontos
        break
    if len(points) == 4:
        break

# Captura o comprimento de referência na imagem original
ref_points_original = []
cv2.setMouseCallback("Image", click_reference_points_original)

print("Clique nos dois pontos que definem o comprimento de referência (1,37 metros):")

while True:
    cv2.imshow("Image", image)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # Pressione 'Esc' para sair sem selecionar os pontos
        break
    if len(ref_points_original) == 2:
        break

cv2.destroyAllWindows()

if len(points) == 4 and len(ref_points_original) == 2:
    # Definir os pontos de destino para a transformação de perspectiva
    width, height = 300, 400
    dst_points = np.array([
        [0, 0],
        [width - 1, 0],
        [width - 1, height - 1],
        [0, height - 1]
    ], dtype="float32")

    # Calcular a matriz de transformação de perspectiva
    src_points = np.array(points, dtype="float32")
    M = cv2.getPerspectiveTransform(src_points, dst_points)

    # Aplicar a transformação de perspectiva
    warped = cv2.warpPerspective(orig, M, (width, height))

    # Calcular o comprimento do traço de referência em pixels na imagem original
    ref_length_pixels_original = euclidean_distance(ref_points_original[0], ref_points_original[1])
    reference_length_meters = 1.37
    scale = reference_length_meters / ref_length_pixels_original

    # Medir as dimensões da quadra na imagem transformada (em pixels)
    top_left = (0, 0)
    top_right = (warped.shape[1] - 1, 0)
    bottom_left = (0, warped.shape[0] - 1)
    bottom_right = (warped.shape[1] - 1, warped.shape[0] - 1)

    width_pixels = euclidean_distance(top_left, top_right)
    height_pixels = euclidean_distance(top_left, bottom_left)

    # Calcular as dimensões reais
    width_meters = width_pixels * scale
    height_meters = height_pixels * scale
    half_length_meters = height_meters / 2

    # Medidas oficiais da quadra de tênis
    official_width = 10.97  # Em metros
    official_height = 23.77  # Em metros

    # Exibir a imagem transformada
    cv2.imshow("Warped Image", warped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Imprimir as medidas
    print(f"Comprimento do traço de referência na imagem original em pixels: {ref_length_pixels_original:.2f}")
    print(f"Escala: {scale:.2f} metros por pixel")
    print(f"\nMedidas Oficiais da Quadra:")
    print(f"Largura: {official_width} metros")
    print(f"Comprimento: {official_height} metros")
    print(f"Comprimento de cada metade: {official_height / 2} metros")

    print(f"\nMedidas Obtidas após a Transformação:")
    print(f"Largura: {width_meters:.2f} metros")
    print(f"Comprimento: {height_meters:.2f} metros")
    print(f"Comprimento de cada metade: {half_length_meters:.2f} metros")
