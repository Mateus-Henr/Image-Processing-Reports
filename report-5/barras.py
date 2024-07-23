import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = 'barras.png'
image = cv2.imread(image_path)

rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
R, G, B = rgb_image[:, :, 0], rgb_image[:, :, 1], rgb_image[:, :, 2]

hsv_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2HSV)
H, S, V = hsv_image[:, :, 0], hsv_image[:, :, 1], hsv_image[:, :, 2]

plt.figure(figsize=(10, 6))
plt.subplot(2, 3, 1)
plt.plot(R[200], label='Vermelho', color='Red')
plt.plot(G[200], label='Verde', color='Green')
plt.plot(B[200], label='Azul', color='Blue')
plt.title('Evolução do RGB')
plt.xlabel('Width')
plt.ylabel('RGB Value')
plt.legend()

plt.subplot(2, 3, 2)
plt.plot(H[200], label='Hue')
plt.title('Evolução do HUE')
plt.xlabel('Width')
plt.ylabel('Hue')

plt.subplot(2, 3, 3)
plt.plot(S[200], label='Saturação')
plt.title('Evolução da Saturação')
plt.xlabel('Width')
plt.ylabel('Saturação')

plt.subplot(2, 3, 4)
plt.plot(V[200], label='Value')
plt.title('Evolução do Value')
plt.xlabel('Width')
plt.ylabel('Value')

plt.tight_layout()
plt.show()
