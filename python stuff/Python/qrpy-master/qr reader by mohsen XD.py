from PIL import Image
import zbarlight
import cv2 as cv
####################################
cap = cv.VideoCapture(0)

while True:
    _,frame = cap.read()
    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    image = Image.fromarray(frame)

    cv.imshow('frame',frame)
    codes = zbarlight.scan_codes('qrcode', image)
    print('QR codes: %s' % codes)
    
    ikey = cv.waitKey(5)
    if (ikey==ord("q")):
        cv.destroyAllWindows()
        break
