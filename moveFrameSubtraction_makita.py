# -*- coding: UTF-8 -*-
# anaconda3-2.5.0

import cv2
import math
import numpy as np
import os
import csv

if __name__ == '__main__':

    # 動画読み込み
    cap = cv2.VideoCapture('./materials/MAH00331.MP4')
    '''
    width = cap.get(3)
    height = cap.get(4)
    print(height, width)
    '''

    # カメラから読み込む
    # cap = cv2.VideoCapture(0)

    # 学習用画像のサイズ
    studyX = 30
    studyY = 30

    # 整数サイズに
    studyX = int(studyX / 2)
    studyY = int(studyY / 2)

    # logヘッダー用
    logHeader = 0

    # 時刻tのフレーム画像
    sorceImg1 = None
    # 時刻t+1のフレーム画像
    sorceImg2 = None
    # 時刻t+2のフレーム画像
    sorceImg3 = None

    # ログ用csv
    logFile = open('./log.csv','w')
    logWriter = csv.writer(logFile, lineterminator = '\n')
    frameNum = 0
    noizFrameNum = 0
    header = []     # header用
    listData = []   # listの初期化
    poiIndex = 0

    # 学習用画像の名前
    filename = "./studyMaterial/image"

    while 1:
        # フレーム取得
        ret, frame = cap.read()

        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

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

            # グレースケール化
            grayResultImg = cv2.cvtColor(resultImg, cv2.COLOR_BGR2GRAY)

            labelingResults = cv2.connectedComponentsWithStats(grayResultImg, 8, cv2.CV_8U)

            # ポインタくらいの大きさのインデックスを探す
            arraySize = len(labelingResults[2])
            # ポインタくらいの大きさがあれば1, それ以外は0を返す
            for i in range(arraySize):
                if labelingResults[2][i][4] >= 100 and labelingResults[2][i][4] <= 500:
                    print (labelingResults[2][i][4])
                    poiIndex = i
                    break
                else:
                    poiIndex = 0


            # cv2.imwrite("./makedata/diffImg1_2.png", diffImg1_2)
            # cv2.imwrite("./makedata/diffImg2_3.png", diffImg2_3)

            # log書き込み
            listData.append(frameNum)
            leftUpX = labelingResults[2][poiIndex][0]
            leftUpY = labelingResults[2][poiIndex][1]
            middleX = int(labelingResults[3][poiIndex][0])
            middleY = int(labelingResults[3][poiIndex][1])
            listData.append(middleX)  #中心座標x
            listData.append(middleY)  #中心座標y
            listData.append(leftUpX)    # 左上x
            listData.append(leftUpY)    # 左上y

            if logHeader == 0:
                logHeader = 1
                print("head")
                header.append("フレーム数,中心座標X,中心座標Y,左上x,左上y")
                logWriter.writerow(header)

            # 学習用画像生成
            if poiIndex != 0:
                if noizFrameNum > 4:    # 端部から認識する場合、ノイズになりうる
                    logWriter.writerow(listData)    # log.csvへの書き込みを行う
                    writefilename = filename + str(frameNum) + '.png'
                    #dst = resultImg[middleY-studyY:middleY+studyY, middleX-studyX:middleX+studyX]
                    dst = sorceImg2[middleY-studyY:middleY+studyY, middleX-studyX:middleX+studyX]
                    cv2.imwrite(writefilename, dst)
                    img = cv2.imread(writefilename)
                    # cv2.imshow("makeImg", img) # なぜか動かない

                else:
                    noizFrameNum += 1

            del listData[:]
            leftUpX = 0
            leftUpY = 0
            middleX = 0
            middleY = 0
            frameNum += 1

            #表示
            cv2.imshow("FRAMES", resultImg)

        # qで終了
        k = cv2.waitKey(1)
        if k == ord('q'):
            # print(cv2.connectedComponents(resultImg))

            logFile.close()

            # csvでラベリング結果を保存する
            with open('./labeling.csv', 'w') as f:
                # 改行コードの指定
                writer = csv.writer(f, lineterminator = '\n')

                # 2次元配列も書き込める
                writer.writerows(cv2.connectedComponents(grayResultImg)[1])
                print(cv2.connectedComponents(grayResultImg[0]))

                # ラベリング処理(詳細版): 8点見るか4点見るかの8
                labelingResults = cv2.connectedComponentsWithStats(grayResultImg, 8, cv2.CV_8U)
                print(labelingResults[0] - 1)
                print(labelingResults[1])
                print(labelingResults[2])
                print(labelingResults[3])


            break

    cap.release()
    cv2.destroyAllWindows()
