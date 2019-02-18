import numpy as np
import cv2 as cv

def map( x, in_min,in_max, out_min, out_max):
    maps = -((x - in_max)*(out_max-out_min)/(in_max-in_min)+out_min)
    return maps
def nothing(x):
    pass    

webcam = cv.VideoCapture(0)
minf = np.array([20,169,63])
maxf = np.array([71,255,182])

######################
#hsv,hsvblured,binary,medianed,im2,contours,hierarchy,ycnt,xcnt,cnt,radius,center = np.zeros((12, 5))
hsv = [0,0,0,0]
hsvblured = [0,0,0,0]
binary = [0,0,0,0]
medianed = [0,0,0,0]
im2 = [0,0,0,0]
contours = [0,0,0,0]
hierarchy = [0,0,0,0]
window = ['wcp1','wcp2','wcp3','wcp4']
window2 = ['wccp1','wccp2','wccp3','wccp4']
window3 = ['wcccp1','wcccp2','wcccp3','wcccp4']
################################################
while True:
    _,frame = webcam.read()
    mrkzy = int(len(frame)/2)
    mrkzx = int(len(frame[0])/2)
    xframe = len(frame[0])
    yframe = len(frame)
    ycnt = [0,0,0,0]
    xcnt = [0,0,0,0]
    cnt = [0,0,0,0]
    radius = [0,0,0,0]
    center = [0,0,0,0]
    cropped = [frame[0:yframe, 0:160] , frame[0:yframe, 480:640] , frame[0:120, 0:xframe] , frame[360:480, 0:xframe] ]
    
    hsvfr = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    hsvbluredfr = cv.GaussianBlur(hsvfr, (5, 5), 0)
    binaryfr = cv.inRange(hsvbluredfr, minf, maxf)
    medianedfr = cv.medianBlur(binaryfr, 25)
    filteredfr = cv.bitwise_and(frame,frame, mask= medianedfr)
    im2fr, contoursfr, hierarchyfr = cv.findContours(medianedfr,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

    for d in range(0,4):
        hsv[d] = cv.cvtColor(cropped[d], cv.COLOR_BGR2HSV)
        hsvblured[d] = cv.GaussianBlur(hsv[d], (5, 5), 0)
        binary[d] = cv.inRange(hsvblured[d], minf, maxf)
        medianed[d] = cv.medianBlur(binary[d], 25)
        im2[d], contours[d], hierarchy[d] = cv.findContours(medianed[d],cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)  

    try:  
        if len(contoursfr) > 0:
            cntfr = max(contoursfr, key = cv.contourArea)
            (xfr,yfr), radiusfr = cv.minEnclosingCircle(cntfr) 
            centerfr = (int(xfr),int(yfr)) 
            cv.circle(frame,centerfr,2,(255,0,0),2)
            xfr,yfr,wfr,hfr = cv.boundingRect(cntfr)
            cv.rectangle(frame,(xfr,yfr),(xfr+wfr,yfr+hfr),(0,255,0),2)
            for f in range (0,4):
                if (len(contours[f])>0):
                    cnt[f] = max(contours[f], key = cv.contourArea)
                    (xcnt[f],ycnt[f]), radius[f] = cv.minEnclosingCircle(cnt[f])     
                    center[f] = (int(xcnt[f]),int(ycnt[f]))
                    radius[f] = int(radius[f])
                    cv.circle(cropped[f],center[f],radius[f],(0,0,255),2)
                    cv.circle(cropped[f],center[f],2,(255,0,0),2)
            
    except Exception as excerr:
        print(excerr)
################################################
    for i in range(0,4):
        #cv.imshow(window[i], cropped[i])
        cv.imshow("frame", frame)
        print(center[i])
################################################
    ikey = cv.waitKey(5)
    if (ikey==ord("q")):
        cv.destroyAllWindows()
        break
