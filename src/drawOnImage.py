import numpy as np
import cv2 as cv
import cv2

#Lowkey broken
def draw(event,x,y,flags,param):
    while(cv.EVENT_LBUTTONDOWN == True):
        cv.line(img,(x,y),(x+10,y+10),(255,0,0),5)
        print("hello")
        if cv.EVENT_LBUTTONDOWN == False:
            break
        


img = cv2.imread("test-images/screenshot.JPG")
cv.namedWindow('image')
cv.setMouseCallback('image',draw)
while(1):
    cv.imshow('image',img)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()