#
#   RGB -> HSVしHueとSaturationについてpls回帰分析
#
import numpy as np
import cv2
import csv

from numpy.random import *

DATASIZE = 13   # 教師用画像の大きさ

# 2次元のガウス確率密度(正規分布)を導出-------------
def Gauss2d():
    x = y = np.arange(-6, 7, 1)
    X, Y = np.meshgrid(x, y)

    # 平均と分散
    mu = np.array([0, 0])
    sigma = np.array([[10, 0],[0, 10]])

    # 行列式を計算
    det = np.linalg.det(sigma)

    # 逆行列を計算
    inv_sigma = np.linalg.inv(sigma)

    # Gauss二次元確率密度を返す関数
    def f(x, y):
        x_c = np.array([x, y]) - mu
        return np.exp(- x_c.dot(inv_sigma).dot(x_c[np.newaxis, :].T)/2.0) \
        / (2 * np.pi * np.sqrt(det))

    # 配列それぞれに対応するものを返す関数に変える
    Z = np.vectorize(f)(X, Y)

    return Z

# RGBをR要素, G要素, B要素に分割-----------------
def RGB2RGB(img):
    # RGB分割 0:B 1:G R:2 に分ける
    rgb = cv2.split(img)
    blue  = rgb[0]
    green = rgb[1]
    red   = rgb[2]

    return(red, green, blue)

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

# pls回帰によるHS成分分析----------------

# 2次元の正規分布を生成　13*13
nD = Gauss2d() # normal distribution

dataNumArray = []
imageAddress = "../studyMaterial/image" # 学習用画像の場所

# csvファイルからフレーム情報を取得
with open("../log.csv", 'r') as f:
    reader = csv.reader(f)
    header = next(reader) # ヘッダーを飛ばす

    # リストに画像番号のみを格納
    for row in reader:
        dataNumArray.append(row[0])

# リストにある番号の画像(教師用データ)をテキストに書き込む
rgbFile = open("RGB.txt", "wt", encoding = "UTF-8")
hsvFile = open("HSV.txt", "wt", encoding = "UTF-8")
ycrcbFile = open("YCrCb.txt", "wt", encoding = "UTF-8")
allFile = open("ALL.txt", "wt", encoding = "UTF-8")

rgbHeader = "W R G B\n"
hsvHeader = "W H S V\n"
ycrcbHeader = "W Y Cr Cb\n"
allHeader = "W R G B H S V Y Cr Cb\n"

rgbFile.write(rgbHeader)
hsvFile.write(hsvHeader)
ycrcbFile.write(ycrcbHeader)
allFile.write(allHeader)

for i in range(30):
    # ランダムな画像を選択
    teacherNum = randint(0, len(dataNumArray))

    # 教師用画像の名前を生成
    imageName = imageAddress + dataNumArray[teacherNum] + ".png"
    print(imageName)
    # 画像取得
    img = cv2.imread(imageName, 1)

    # 特徴量分割
    R, G, B = RGB2RGB(img)
    H, S, V = RGB2HSV(img)
    Y, Cr, Cb = RGB2YCrCb(img)

    # テキストに書き込む文字列を生成
    for j in range(DATASIZE):
        for k in range(DATASIZE):
            rgbData = str(nD[j][k]) + " " + str(R[j][k]) + " " + str(G[j][k]) + " " + str(B[j][k]) + "\n"
            hsvData = str(nD[j][k]) + " " + str(H[j][k]) + " " + str(S[j][k]) + " " + str(V[j][k]) + "\n"
            ycrcbData = str(nD[j][k]) + " " + str(Y[j][k]) + " " + str(Cr[j][k]) + " " + str(Cb[j][k]) + "\n"
            allData = rgbData.rstrip("\n") + " " + \
                      str(H[j][k]) + " " + str(S[j][k]) + " " + str(V[j][k]) + " " + \
                      str(Y[j][k]) + " " + str(Cr[j][k]) + " " + str(Cb[j][k]) + "\n"

            # ファイルに書き込む
            rgbFile.write(rgbData)
            hsvFile.write(hsvData)
            ycrcbFile.write(ycrcbData)
            allFile.write(allData)

rgbFile.close()
hsvFile.close()
ycrcbFile.close()
allFile.close()
