import cv2
import numpy as np

filename = 'quadra1.png'
img = cv2.imread(filename)
img = cv2.GaussianBlur(img, (5, 5), 0)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_mask = np.array([0, 50, 50])
upper_mask = np.array([255, 255, 255])
mask = cv2.inRange(hsv, lower_mask, upper_mask)
masked_img = cv2.bitwise_and(img, img, mask=mask)

gray = cv2.cvtColor(masked_img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)  # Adjusted parameters

dst = cv2.dilate(dst, None)

threshold = 0.05 * dst.max()  # Increased threshold
img[dst > threshold] = [0, 0, 255]

corners = np.argwhere(dst > threshold)

# Apply non-maximum suppression
filtered_corners = []
for corner in corners:
    y, x = corner
    if len(filtered_corners) == 0 or all(np.linalg.norm(np.array((x, y)) - np.array(fc)) > 100 for fc in filtered_corners):
        filtered_corners.append((x, y))
        print(f"Canto: ({x}, {y})")

cv2.imshow('dst', img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
