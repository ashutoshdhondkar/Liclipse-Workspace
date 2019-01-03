import cv2
import numpy
import matplotlib.pyplot as plt
import time


cap = cv2.VideoCapture(0)
# 0 : first webcam
# 1 : second webcam

# time.sleep(2)
while(True):
    ret,frame = cap.read()
    # frame will be the next frame in camera
    # ret is a boolean variable
     
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',frame)  
    cv2.imshow('gray',gray)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
    
cap.release()

cv2.destroyAllWindows()