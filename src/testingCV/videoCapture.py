import cv2

cap = cv2.VideoCapture("test-images/test_Trim.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(100) & 0xFF == ord('q'):  # Press 'q' to quit
        break
