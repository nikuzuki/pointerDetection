#coding=utf-8

import cv2
import numpy as np

def export_movie():

    # 入力する動画と出力パスを指定。
    target = "./materials/hikaku1_white.mp4"
    result = "./materials/hikaku1_white.m4v"

    # 動画の読み込みと動画情報の取得
    movie = cv2.VideoCapture(target)
    fps    = movie.get(cv2.CAP_PROP_FPS)
    height = movie.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width  = movie.get(cv2.CAP_PROP_FRAME_WIDTH)
    frameNum = 0;

    # 形式はMP4Vを指定
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

    # 出力先のファイルを開く
    out = cv2.VideoWriter(result, int(fourcc), fps, (int(width), int(height)))

    # 最初の1フレームを読み込む
    if movie.isOpened() == True:
        ret,frame = movie.read()
    else:
        ret = False

    # フレームの読み込みに成功している間フレームを書き出し続ける
    while ret:
        print(str(frameNum) + " / 1500")
        frameNum = frameNum + 1
        # 画像を別の特徴量に変換
        hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        ycrcbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)

        # 加工用の配列を生成
        imageArray = np.zeros((height, width))

        print(imageArray.shape)

        maxData = -1.0
        maxX = -1
        maxY = -1

        # 各画素にアクセス
        for i in range(int(height)):
            for j in range(int(width)):
                pixelValueRGB = frame[i, j]    # [B, G, R]
                pixelValueHSV = hsvImage[i, j] # [H, S, V]
                pixelValueYCrCb = ycrcbImage[i, j] # [Y, Cr, Cb]

                b, g, r = pixelValueRGB[:3]
                h, s, v = pixelValueHSV[:3]
                y, cr, cb = pixelValueYCrCb[:3]
                #print("rgb", b, g, r)
                #print("hsv", h, s, v)
                #print("ycrcb", y, cr, cb)

                imageArray[i, j] = r * 7.528200e-04 + \
                                   g * 1.244851e-04 + \
                                   b * -1.428965e-04 + \
                                   h * -2.149440e-06 + \
                                   s * -1.096108e-05 + \
                                   v * 1.077122e-04 + \
                                   y * -7.389134e-04 + \
                                  cr * -9.388121e-04 + \
                                  cb *  2.879901e-04
                if maxData < imageArray[i, j]:
                    maxData = imageArray[i, j]
                    maxX = j
                    maxY = i
                    #print("if do")

        print(maxData, maxX, maxY)
        #img[maxX,maxY] = [0,0,0]
        cv2.circle(frame, (maxX,maxY), 10, (0,0,0),-1)
        cv2.imshow("making", frame)
        # 読み込んだフレームを書き込み
        out.write(frame)
        maxData = 0
        maxX = 0
        maxY = 0

        # 次のフレームを読み込み
        ret,frame = movie.read()


if __name__ == '__main__':
    export_movie()
