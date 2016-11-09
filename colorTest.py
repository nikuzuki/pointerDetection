import numpy as np
import cv2

im = cv2.imread("black.ppm")
RGB = cv2.split(im)
Blue   = RGB[0]
Green = RGB[1]
Red    = RGB[2]


cv2.imshow("Blue",Blue)
cv2.imshow("Green",Green)
cv2.imshow("Red",Red)

k = cv2.waitKey()
