import cv2
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Sets width of window to 640px
cap.set(4, 480)  # Sets height of window to 480px
cap.set(10, 100)  # Sets brightness to 100


while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(100) & 0xFF == ord('q'):  # Press 'q' to quit
        break
