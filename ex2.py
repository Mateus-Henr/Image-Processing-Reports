import numpy as np
import cv2

boundaries = {
    'green': [[60, 50, 50], [80, 255, 255]],  # Hue: 60-80, Saturation: 50-255, Value: 50-255
    'yellow': [[20, 100, 100], [30, 255, 255]],  # Hue: 20-30, Saturation: 100-255, Value: 100-255
    'red': [[160, 100, 100], [190, 255, 255]],  # Hue: 160-180, Saturation: 100-255, Value: 100-255
    'grey': [[0, 0, 100], [179, 50, 200]],  # Hue: 0-179, Saturation: 0-50, Value: 100-200
    'black': [[0, 0, 0], [179, 50, 50]],  # Hue: 0-179, Saturation: 0-50, Value: 0-50
    'blue': [[101, 50, 38], [110, 255, 255]],  # Hue: 101-110, Saturation: 50-255, Value: 38-255
}

cap = cv2.VideoCapture(0)  # cap = cv2.VideoCapture("video.mp4")
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 60.0, (1920, 1080))
counter = 0

print('Colours')
for colour in boundaries:
    print(colour)
colour = input('Type the colour that you desire:')

if colour not in boundaries:
    print('Invalid colour')
    exit()

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(frame, boundaries[colour][0], boundaries[colour][1])

    out.write(frame)
    cv2.imshow('Original', frame)

    counter += 1
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
