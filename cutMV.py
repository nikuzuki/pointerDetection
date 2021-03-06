# coding: utf-8
import numpy as np
import cv2

# 素材となる動画
cap = cv2.VideoCapture('./materials/hikaku2.MP4')
count = 0
filename = "./testData2/test"

while cap.isOpened():
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imshow('frame', frame)
    if count % 10 == 0:
        writefilename = filename + str(int(count / 10)) + '.png'
        cv2.imwrite(writefilename, frame)

    count = count + 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
