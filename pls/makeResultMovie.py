#
#   ポインタ検出(学習結果)かつ動画作成
#
import numpy as np
import cv2

from numpy.random import *

dataNumArray = []
imageAddress = "../makedata/test"
cap = cv2.VideoCapture('./materials/hikaku2.MP4')

# RGB -> HSV変換関数--------------------------
def RGB2HSV(img):

    # HSV変換
    hsvImage = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hsv = cv2.split(hsvImage)
    hue        = hsv[0]         # 0 ~ 179 (*2)
    saturation = hsv[1]         # 0 ~ 255
    value      = hsv[2]         # 0 ~ 255

    return(hue, saturation, value)

# RGB -> YCrCb変換関数--------------------------
def RGB2YCrCb(img):

    # YCrCb変換
    ycrcbImage = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    ycrcb = cv2.split(ycrcbImage)
    y  = ycrcb[0]
    cr = ycrcb[1]
    cb = ycrcb[2]

    return(y, cr, cb)

# ランダムな画像を取得, 最大値の場所を探す
while(cap.isOpened()):
    # フレーム読み込み
    ret, frame = cap.read()
    if ret == True:
        

    # 画像取得
    img = cv2.imread(imageName, 1)
    hsvImage = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    ycrcbImage = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

    height, width = img.shape[:2]
    imageArray = np.zeros((height, width))

    print(imageArray.shape)

    maxData = -1.0
    maxX = -1
    maxY = -1

    # 各画素にアクセス
    for i in range(height):
        for j in range(width):
            pixelValueRGB = img[i, j]    # [B, G, R]
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
            #print("check", i, j, maxData, imageArray[i, j])

            if maxData < imageArray[i, j]:
                maxData = imageArray[i, j]
                maxX = j
                maxY = i
                #print("if do")
    print(maxData, maxX, maxY)
    #img[maxX,maxY] = [0,0,0]
    cv2.circle(img, (maxX,maxY), 10, (0,0,0),-1)
    cv2.imshow("img",img)
    cv2.waitKey()
