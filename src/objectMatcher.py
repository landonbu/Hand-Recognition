import cv2 as cv
import numpy as numpy
from matplotlib import pyplot as plt

#Create ORB object and imports image
img = cv.imread("test-images/screenshot.JPG" , 0)
orb=cv.ORB_create()
#Defines keypoints on image
keypoints = orb.detect(img,None)
#Calculates the keypoints on the image, and creates a second image with said keypoints
keypoints , des = orb.compute(img,keypoints)
img2 = cv.drawKeypoints(img , keypoints , None , color=(255,0,0) , flags=0)
#Displays the keypoints on the image using matplot
plt.imshow(img2), plt.show()

