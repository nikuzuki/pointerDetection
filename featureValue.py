# -*- coding: UTF-8 -*-

import cv2
import math
import numpy as np
import os
import sys

if __name__ == '__main__':

    # 動画読み込み 330:円に緑 328:緑に緑
    cap = cv2.VideoCapture('./materials/MAH00328.MP4')

    while(cap.isOpened()):

        # フレーム取得
        ret, frame = cap.read()

        # RGB分割 0:B 1:G R:2 に分ける
        RGB = cv2.split(frame)
        Blue = RGB[0]
        Green = RGB[1]
        Red = RGB[2]

        # HSV分割
        # HSV = cv2.split(cv2.cvtColor(frame))
        image_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        HSV = cv2.split(image_hsv)
        Hue = HSV[0]        # 0 ~ 179 (*2)
        Saturation = HSV[1] # 0 ~ 255
        Value = HSV[2]      # 0 ~ 255


        cv2.imshow("source", frame)
        cv2.imshow("Blue", Blue)
        cv2.imshow("Green", Green)
        cv2.imshow("Red", Red)
        # cv2.imshow("HSV_image", image_hsv)
        cv2.imshow("Hue", Hue)
        cv2.imshow("Saturation", Saturation)
        cv2.imshow("Value", Value)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
