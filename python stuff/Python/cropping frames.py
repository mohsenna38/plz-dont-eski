import numpy as np
import cv2 as cv

webcam = cv.VideoCapture(0)
###################################
while(True):
    _,frame = webcam.read()
##################

    cropped = frame[100:100+100, 100:100+100]

##################
    cv.imshow("frame", frame)
    cv.imshow("frameasd", cropped)
###################################
    ikey = cv.waitKey(1)
    if(ord("q") == ikey):
        break
cv.destroyAllWindows()
 
