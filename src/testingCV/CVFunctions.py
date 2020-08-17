import cv2
import numpy as np

img = cv2.imread("test-images/screenshot.JPG")
kernel = np.ones((5, 5), np.uint8)

# Makes the image gray
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Ryan's Comment :)

# Blurs the image
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)

# Detects edges
imgCanny = cv2.Canny(img, 100, 100)

# Makes edges thicker
imgDialation = cv2.dilate(
    imgCanny, kernel, iterations=1)

# Makes edges thinner
imgEroded = cv2.erode(
    imgCanny, kernel, iterations=1)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blurred Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilated Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)

# Prints image dimensions
print(img.shape)

# Resizes the image to the following dimensions (width, height)
imageReSize = cv2.resize(img, (300, 200))

# Crops the image [height endpoints, width endpoints]
imageCropped = img[0:200, 200:500]


cv2.waitKey(0)
