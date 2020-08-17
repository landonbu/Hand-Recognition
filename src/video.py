import cv2
import numpy as np

cap = cv2.VideoCapture("test-images/screenshot.JPG")

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(5000) & 0xFF == ord('q'):  # Press 'q' to quit
        break
