import cv2
import numpy as np

not_white = [[120, 110, 110], [250, 250, 250]]

# Boundaries for the colours
boundaries = {
    'green': [[60, 50, 50], [80, 255, 255]],  # Hue: 60-80, Saturation: 50-255, Value: 50-255
    'yellow': [[20, 100, 100], [30, 255, 255]],  # Hue: 20-30, Saturation: 100-255, Value: 100-255
    'red': [[160, 100, 100], [190, 255, 255]],  # Hue: 160-180, Saturation: 100-255, Value: 100-255
    'grey': [[0, 0, 100], [179, 50, 200]],  # Hue: 0-179, Saturation: 0-50, Value: 100-200
    'black': [[0, 0, 0], [179, 50, 50]],  # Hue: 0-179, Saturation: 0-50, Value: 0-50
    'blue': [[101, 50, 38], [110, 255, 255]],  # Hue: 101-110, Saturation: 50-255, Value: 38-255
}


def replace_colour(img):
    # Define the lower and upper bounds of the color range to replace
    not_white_lower = np.array([140, 140, 140])
    not_white_upper = np.array([254, 254, 254])

    mask_white = cv2.inRange(img, not_white_lower, not_white_upper)
    img[np.where(mask_white != 0)] -= 60  # Replace non-white pixels with black

    return img

def get_processed_hsv_img(original_img):
    hsv = cv2.cvtColor(original_img, cv2.COLOR_BGR2HSV)

    # Create a mask for each color range
    masks = {color: cv2.inRange(hsv, np.array(boundaries[color][0]), np.array(boundaries[color][1])) for color in
             boundaries}

    # Replace colors based on the masks
    for color in masks:
        hsv[np.where(masks[color] != 0)] = boundaries[color][1]

    # Convert the modified HSV image back to BGR color space
    modified_img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return modified_img


img = cv2.imread('halteres.jpg')

processed_img = get_processed_hsv_img(img)

# Display the modified image
cv2.imshow("Halter", replace_colour(processed_img))

# Wait for ESC key to exit
while True:
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        cv2.destroyAllWindows()
        break
