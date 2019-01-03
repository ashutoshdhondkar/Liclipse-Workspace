import numpy
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('datasets\watch.jpg')

# drawing a line on an image
cv2.line(img,(0,0),(100,50),(255,0,0),5)

# drawing a rectangle on an image
cv2.rectangle(img,(0,0),(100,100),(255,255,0),5)

# drawing a circle on image
cv2.circle(img,(100,100),55,(0,0,255),5)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Best watch',(0,50),font,1,(0,0,0),5)
cv2.imshow('image',img)

cv2.waitKey(0)

cv2.destroyAllWindows()