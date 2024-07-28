import cv2
import numpy as np

filename = 'quadra1.png'
img = cv2.imread(filename)

# Apply Gaussian Blur to reduce noise
img = cv2.GaussianBlur(img, (5, 5), 0)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_mask = np.array([0, 50, 50])
upper_mask = np.array([255, 255, 255])
mask = cv2.inRange(hsv, lower_mask, upper_mask)

# Apply the mask to the original image to isolate red and green regions
masked_img = cv2.bitwise_and(img, img, mask=mask)

# Convert to grayscale
gray = cv2.cvtColor(masked_img, cv2.COLOR_BGR2GRAY)

# Convert to float32 for corner detection
gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 10, 5, 0.21)

# Dilate the result to mark the corners
dst = cv2.dilate(dst, None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst > 0.01 * dst.max()] = [0, 0, 255]

cv2.imshow('dst', img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
