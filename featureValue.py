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

        # 0:B 1:G R:2 に分ける
        RGB = cv2.split(frame)
        Blue = RGB[0]
        Green = RGB[1]
        Red = RGB[2]

        cv2.imshow("sorce", frame)
        cv2.imshow("Blue", Blue)
        cv2.imshow("Green", Green)
        cv2.imshow("Red", Red)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
