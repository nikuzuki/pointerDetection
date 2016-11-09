import numpy as np
import cv2
import csv

img0 = cv2.imread("./black.ppm")
print(img0)

# while 1:
    # cv2.imshow("img", img)

#img = cv2.cvtColor(img0, cv2.COLOR_BGR2RGB)

yuv = cv2.cvtColor(img0, cv2.COLOR_BGR2YCrCb)
print(yuv)
YCrCb = cv2.split(yuv)
print(YCrCb[0])
img2 = cv2.cvtColor(yuv, cv2.COLOR_YCrCb2BGR)

cv2.imshow("img", img2)

k = cv2.waitKey()
