from __future__ import division
from __future__ import print_function
from argparse import ArgumentParser
import cv2 as cv
import apriltag
###/################################
webcam = cv.VideoCapture(0)
cv.namedWindow('window')
tagid = 8
###/################################
def nothing(x):
    pass    
####################################
cv.createTrackbar('smt1', 'window',0,10,nothing)
cv.createTrackbar('smt2', 'window',0,10,nothing)
cv.createTrackbar('smt3', 'window',0,10,nothing)
cv.createTrackbar('smt4', 'window',0,10,nothing)
###/################################
parser = ArgumentParser(description='test apriltag Python bindings')
parser.add_argument('device_or_movie', metavar='INPUT', nargs='?', default=0,help='Movie to load or integer ID of camera device')
apriltag.add_arguments(parser)
options = parser.parse_args()
detector = apriltag.Detector(options,searchpath=apriltag._get_demo_searchpath())
###/################################
while True:
    _, frame = webcam.read()
    mrkzy = int(len(frame)/2)
    mrkzx = int(len(frame[0])/2)
    xframe = len(frame[0])
    yframe = len(frame)
    smt1 = cv.getTrackbarPos('smt1','window')
    smt2 = cv.getTrackbarPos('smt2','window')
    smt3 = cv.getTrackbarPos('smt3','window')
    smt4 = cv.getTrackbarPos('smt4','window')
    gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
    detections, dimg = detector.detect(gray, return_image=True)
    hilight = frame // 2 + dimg[:, :, None] // 2 

######################################################################
    try:
        for L in range (len(detections)):
            dtid = detections[L][1]
            if (dtid == tagid):
                dtcord = detections[L][6]
                aprilx = int(detections[L][6][0])
                aprily = int(detections[L][6][1])
                center = (aprilx,aprily)
                cv.circle(frame,center,20,(0,0,255),2)
                cv.circle(frame,center,2,(255,0,0),4)
                print(dtcord)
        
######################################################################
    except:
        print("nothin found")
################################### 
    cv.imshow('window', hilight)
    cv.imshow('frame', frame)
###################################
    ikey = cv.waitKey(1)
    if(ord("q") == ikey):
        break
cv.destroyAllWindows()
