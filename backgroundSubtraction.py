# coding: utf-8
import numpy as np
import cv2

cap = cv2.VideoCapture('./materials/MAH00331.MP4')

# fgbg = cv2.BackgroundSubtractorMOG()
fgbg = cv2.BackgroundSubtractorMOG2()
while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    cv2.imshow('frame', fgmask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
