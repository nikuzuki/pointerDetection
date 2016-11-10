#
#   ポインタ検出(学習結果)かつ動画作成
#
import numpy as np
import cv2

from numpy.random import *

dataNumArray = []
imageAddress = "../makedata/test"
cap = cv2.VideoCapture('../materials/MAH00320.MP4')
#cap = cv2.VideoCapture('./materials/hikaku2.MP4')
#cap = cv2.imread('../sunTest/test107.png')
'''
# RGB -> HSV変換関数--------------------------
def RGB2HSV(img):

    # HSV変換
    hsvImage = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hsv = cv2.split(hsvImage)
    hue        = hsv[0]         # 0 ~ 179 (*2)
    saturation = hsv[1]         # 0 ~ 255
    value      = hsv[2]         # 0 ~ 255

    return(hue, saturation, value)
'''
'''
# RGB -> YCrCb変換関数--------------------------
def RGB2YCrCb(img):

    # YCrCb変換
    ycrcbImage = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    ycrcb = cv2.split(ycrcbImage)
    y  = ycrcb[0]
    cr = ycrcb[1]
    cb = ycrcb[2]

    return(y, cr, cb)
'''

# ランダムな画像を取得, 最大値の場所を探す
while(cap.isOpened()):
#for i in range(1):
    # フレーム読み込み
    ret, img = cap.read()
    #if ret == True:

    # 画像取得
    #img = cv2.imread('../sunTest/test107.png', 1)
    #img = cv2.imread('../sunTest/test107.png', 1)
    hsvImage = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    ycrcbImage = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

    height, width = img.shape[:2]
    imageArray = np.zeros((height, width))
    imageArray_rgb = np.zeros((height, width))
    imageArray_hsv = np.zeros((height, width))
    imageArray_ycbcr = np.zeros((height, width))

    #print(imageArray.shape)

    #maxData = -1.0
    #maxX = -1
    #maxY = -1


    imageArray = img[:,:,2] * 7.528200e-04 + \
                       img[:,:,1] * 1.244851e-04 + \
                       img[:,:,0] * -1.428965e-04 + \
                       hsvImage[:,:,0] * -2.149440e-06 + \
                       hsvImage[:,:,1] * -1.096108e-05 + \
                       hsvImage[:,:,2] * 1.077122e-04 + \
                       ycrcbImage[:,:,0] * -7.389134e-04 + \
                      ycrcbImage[:,:,1] * -9.388121e-04 + \
                      ycrcbImage[:,:,2] *  2.879901e-04

    imageArray_ycbcr = ycrcbImage[:,:,0] * 5.745262e-05 + \
                            ycrcbImage[:,:,1] * 9.182731e-05 + \
                            ycrcbImage[:,:,2] * -4.575109e-06

    imageArray_hsv = hsvImage[:,:,0] * 7.280951e-08 + \
                            hsvImage[:,:,1] * 7.328106e-07 + \
                            hsvImage[:,:,2] * 1.324197e-04

    imageArray_rgb = img[:,:,2] * 6.398149e-05 + \
                            img[:,:,1] * -3.185978e-06 + \
                            img[:,:,0] * -3.206134e-06

    '''
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

            imageArray_ycbcr[i, j] = y * 5.745262e-05 + \
                               cr * 9.182731e-05 + \
                               cb * -4.575109e-06

            imageArray_hsv[i, j] = h * 7.280951e-08 + \
                               s * 7.328106e-07 + \
                               v * 1.324197e-04

            imageArray_rgb[i, j] = r * 6.398149e-05 + \
                               g * -3.185978e-06 + \
                               b * -3.206134e-06




            #print("check", i, j, maxData, imageArray[i, j])
    '''

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(imageArray)
    min_val_ycbcr, max_val_ycbcr, min_loc_ycbcr, max_loc_ycbcr = cv2.minMaxLoc(imageArray_ycbcr)
    min_val_hsv, max_val_hsv, min_loc_hsv, max_loc_hsv = cv2.minMaxLoc(imageArray_hsv)
    min_val_rgb, max_val_rgb, min_loc_rgb, max_loc_rgb = cv2.minMaxLoc(imageArray_rgb)
    imageArray8 = cv2.normalize( imageArray, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

    img[:,:,0] = imageArray8
    img[:,:,1] = imageArray8
    img[:,:,2] = imageArray8

#            if maxData < imageArray[i, j]:
#                maxData = imageArray[i, j]
#                maxX = j
#                maxY = i
#                #print("if do")
#    print(maxData, maxX, maxY)

    #img[maxX,maxY] = [0,0,0]
    #maxX = max_loc[0]
    #maxY = max_loc[1]

    print(str(max_loc) + " , " + str(max_val))

    #cv2.circle(img, (maxX,maxY), 10, (0,0,0),-1)

    cv2.circle(img, max_loc, 10, (255,0,0),2)
    if max_val > -0.057:
        cv2.circle(img, max_loc, 10, (0,0,255),2)

    #cv2.circle(img, max_loc, 10, (0,0,0),2)
    #cv2.circle(img, max_loc, 10, (255,255,255),2)
    #cv2.circle(img, max_loc_ycbcr, 20, (0,0,0),4)
    #cv2.circle(img, max_loc_ycbcr, 20, (255,0,0),2)
    #cv2.circle(img, max_loc_hsv, 25, (0,0,0),4)
    #cv2.circle(img, max_loc_hsv, 25, (0,255,0),2)
    #cv2.circle(img, max_loc_rgb, 30, (0,0,0),4)
    #cv2.circle(img, max_loc_rgb, 30, (0,0,255),2)
    #cv2.circle(img, max_loc, 10, (0,0,0),-1)
    #cv2.imshow("img",imageArray8)
    cv2.imshow("img",img)
    #cv2.waitKey(1))
    if cv2.waitKey(500)  == ord('a'):
        while(1):
            get_key = cv2.waitKey(0)
            if get_key == ord('q'):
                break
