import cv2
import numpy as np

img = np.zeros((512, 512), np.uint8)


def empty(a):
    pass


# print(img)
# img[:] = 0, 0, 0  # Sets the entire image to black.

# shape(image, (height, width), color(RBG), thickness )
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
cv2.rectangle(img, (0, 0), (250, 300), (0, 0, 255), 2)

"""
while True:
    cv2.imshow("Image", img)

    cv2.namedWindow("Trackbar")
    cv2.resizeWindow("Trackbar", 640, 240)
    cv2.createTrackbar("Hue min", "Trackbar", 0, 179, empty)

    h_min = cv2.getTrackbarPos("Hue min", "Trackbar")
    cv2.waitKey(0)
"""
