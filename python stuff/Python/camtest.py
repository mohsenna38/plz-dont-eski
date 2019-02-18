from __future__ import division
from __future__ import print_function
from argparse import ArgumentParser
import cv2 as cv
import apriltag

def main():
    parser = ArgumentParser(description='test apriltag Python bindings')
    parser.add_argument('device_or_movie', metavar='INPUT', nargs='?', default=0,help='Movie to load or integer ID of camera device')
    apriltag.add_arguments(parser)
    options = parser.parse_args()

    webcam = cv.VideoCapture(0)
    cv.namedWindow('frame')

    detector = apriltag.Detector(options,searchpath=apriltag._get_demo_searchpath())

    while True:
        _,frame = webcam.read()
        gray = cv.cvtColor(frame,cv.COLOR_RGB2GRAY)

        detections, dimg = detector.detect(gray, return_image=True)
        num_detections = len(detections)
        print('Detected {} tags.\n'.format(num_detections))
	try:
	    print (detections[0])
	except:
        print ("not found")

        overlay = frame // 2 + dimg[:, :, None] // 2
        
        cv.imshow('frame', overlay)
        ikey = cv.waitKey(1)
        if ikey == ord('q'):
            break

if __name__ == '__main__':
    main()
