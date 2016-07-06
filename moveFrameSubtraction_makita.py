# -*- coding: UTF-8 -*-

import cv2
import math
import numpy as np
import os

if __name__ == '__main__':

    # 動画読み込み
    cap = cv2.VideoCapture('./materials/MAH00321.MP4')

    # カメラから読み込む
    # cap = cv2.VideoCapture(0)

    # 時刻tのフレーム画像
    sorceImg1 = None
    # 時刻t+1のフレーム画像
    sorceImg2 = None
    # 時刻t+2のフレーム画像
    sorceImg3 = None

    while 1:
        # フレーム取得
        ret, frame = cap.read()

        sorceImg3 = sorceImg2
        sorceImg2 = sorceImg1
        sorceImg1 = frame

        # 最初の3フレームを格納するため
        if sorceImg3 is None:

            cv2.imshow("No three frames", sorceImg1)

        else:

            # sorceImg1とsorceImg2との差分を求める(各要素の差分)
            diffImg1_2 = cv2.absdiff(sorceImg1, sorceImg2)

            # sorceImg2とsorceImg3との差分を求める
            diffImg2_3 = cv2.absdiff(sorceImg2, sorceImg3)

            # diffImg1_2とdiffImg2_3の差分を2値化 (thresholdの返り値は2つなので1つだけに)
            diffImg1_2b = cv2.threshold(diffImg1_2, 20, 255, cv2.THRESH_BINARY)[1]
            diffImg2_3b = cv2.threshold(diffImg2_3, 20, 255, cv2.THRESH_BINARY)[1]

            # 二値化された差分画像の共有部分を取得
            andImg = cv2.bitwise_and(diffImg1_2b, diffImg2_3b)

            # 膨張/収縮処理用の配列(uint8は符号なし8bit整数型)
            operator = np.ones((3, 3), np.uint8)

            # 膨張処理
            dilateImg = cv2.dilate(andImg, operator, iterations = 3)

            # 収縮処理
            maskImg = cv2.erode(dilateImg, operator, iterations = 3)

            # マスクをかける
            resultImg = cv2.bitwise_and(sorceImg2, maskImg)

            '''
            cv2.imwrite("./makedata/diffImg1_2.png", diffImg1_2)
            cv2.imwrite("./makedata/diffImg2_3.png", diffImg2_3)
            '''

            #表示
            cv2.imshow("FRAMES", maskImg)

        # qで終了
        k = cv2.waitKey(1)
        if k == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
