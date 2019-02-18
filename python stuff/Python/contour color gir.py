import cv2 as cv
import numpy as np
webcam = cv.VideoCapture(0)

while True:
    _,frame = webcam.read()

    mrkzy = int(len(frame)/2)
    mrkzx = int(len(frame[0])/2)
    fry = int(len(frame))
    frx = int(len(frame[0]))

    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    
    im2, contours, hierarchy = cv.findContours(gray,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

    final = np.zeros(frame.shape,np.uint8)
    mask = np.zeros(gray.shape,np.uint8)
    cv.drawContours(mask,contours,1,255,-1)
    cv.drawContours(final,contours,1,cv.mean(frame,mask),-1)
    
    cv.imshow("frame", frame)
###################################
    ikey = cv.waitKey(1)
    if(ord("q") == ikey):
        break
cv.destroyAllWindows()
 