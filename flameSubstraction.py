# -*- coding: UTF-8 -*-

import cv2
import math
import numpy as np
import os

if __name__ == '__main__':

    # カメラからキャプチャー
    #cap = cv2.VideoCapture(0)

    # 時刻tのフレーム画像
    img_src1 = None
    # 時刻t+1のフレーム画像
    img_src2 = None
    # 時刻t+2のフレーム画像
    img_src3 = None

    while(True):

        # 動画ストリームからフレームを取得
        ret, frame = cap.read()

        img_src1 = img_src2
        img_src2 = img_src3
        img_src3 = frame

        # img_src2 にまだ画像が入れられていない場合
        if img_src1 is None:

            cv2.imshow("Show FLAME SUBSTRACTION Image", img_src3)

        else:

            # img_src1 と img_src2 の差分を求める
            img_diff1_2 = cv2.absdiff(img_src1, img_src2)

            # img_src2 と img_src3 の差分を求める
            img_diff2_3 = cv2.absdiff(img_src2, img_src3)

            # img_diff1_2 と img_diff2_3を二値化
            img_diff1_2b = cv2.threshold(img_diff1_2, 20, 255, cv2.THRESH_BINARY)[1]
            img_diff2_3b = cv2.threshold(img_diff2_3, 20, 255, cv2.THRESH_BINARY)[1]

            # 二値化された差分画像の共有部分を取得
            img_m = cv2.bitwise_and(img_diff1_2b, img_diff2_3b)

            # 膨張処理・収縮処理を行ってマスクを生成
            operator = np.ones((3, 3), np.uint8)
            img_dilate = cv2.dilate(img_m, operator, iterations=3)
            img_mask = cv2.erode(img_dilate, operator, iterations=3)

            # マスクをかける
            img_dst = cv2.bitwise_and(img_src2, img_mask)

            # 表示
            cv2.imshow("Show FLAME SUBSTRACTION Image", img_dst)

        # qを押したら終了。
        k = cv2.waitKey(1)
        if k == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
