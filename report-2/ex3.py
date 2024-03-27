from PIL import Image
import pytesseract
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def apply_wellner_threshold(img, window_size, k):
    # Converte a imagem em escala de cinza
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Calcula a média local usando uma janela deslizante
    mean = cv2.boxFilter(gray, cv2.CV_32F, (window_size, window_size))

    # Aplica a fórmula de Wellner para calcular o limiar
    threshold = mean * (1 + k * (gray - mean) / mean)

    # Aplica o limiar na imagem
    thresholded_img = np.zeros_like(gray)
    thresholded_img[gray >= threshold] = 255

    return thresholded_img


def apply_niblack_threshold(img, window_size, k):
    # Converte a imagem em escala de cinza
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Calcula a média e o desvio padrão locais usando uma janela deslizante
    mean = cv2.blur(gray, (window_size, window_size))
    mean_square = cv2.blur(gray * gray, (window_size, window_size))
    variance = mean_square - mean * mean

    # Calcula o limiar usando a fórmula de Niblack
    threshold = mean + k * np.sqrt(variance)

    # Aplica o limiar na imagem
    thresholded_img = np.zeros_like(gray)
    thresholded_img[gray >= threshold] = 255

    return thresholded_img

def apply_otsu_threshold(img):
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Otsu's thresholding
    _, thresholded_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return thresholded_img

def apply_kmeans_clustering(img, num_clusters):
    # Reshape the image into a 2D array
    pixels = img.reshape((-1, 1))

    # Initialize K-means clustering algorithm
    kmeans = KMeans(n_clusters=num_clusters, random_state=0)

    # Fit K-means to the data
    kmeans.fit(pixels)

    # Get cluster centers and labels
    cluster_centers = np.uint8(kmeans.cluster_centers_)
    labels = kmeans.labels_

    # Map each pixel to its respective cluster center
    clustered_img = cluster_centers[labels]

    # Reshape the clustered image to its original shape
    clustered_img = clustered_img.reshape(img.shape)

    return clustered_img

# Path to the image file
image_path = 'placa1.png'
window_size = 50
k_niblack = -0.9
k_wellner = 0.5

# Open the image using PIL (Python Imaging Library)
img = cv2.imread(image_path)

# Apply Wellner's thresholding
thresholded_img = apply_otsu_threshold(img)

# Convert thresholded image to PIL Image
converted_img = Image.fromarray(apply_kmeans_clustering(thresholded_img, 2))

# Perform OCR on the thresholded image
text = pytesseract.image_to_string(converted_img)

# Print the extracted text
print("Texto extraído: \n" + text)

plt.imshow(converted_img, cmap='gray')
plt.axis('off')  # Desativar os eixos
plt.title('Imagem após a limiarização de OTSU')
plt.show()