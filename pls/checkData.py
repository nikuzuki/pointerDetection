# pls回帰分析結果を

import pyper
import numpy as np
import cv2

from numpy.random import *

r = pyper.R()
r("library(pls)")
r("p.data <- read.table('./ALL.txt', header = T)")
r("p.plsr <- plsr(W ~ ., 9, data = p.data, validation = 'LOO')")
#print(r("summary(p.plsr)"))
#print(r("p.plsr$coefficients"))

pPlsr = r.get("p.plsr$coefficients")

#print(pPlsr)

print(pPlsr[8][8][0])   #[ncomp][num][0]

dataNumArray = []
imageAddress = "../makedata/test"

# ランダムな画像を取得, 最大値の場所を探す
for i in range(1):
    # ランダムな画像を選択
    testNum = randint(0, 111)

    # テスト用画像の名前を生成
    imageName = imageAddress + testNum + ".png"
    print(imageName)

    # 画像取得
    img = cv2.imread(imageName, 1)
    height, width = img.shape[:2]
    imageArray = np.zeros((height, width))

    # 各画素にアクセス
    for i in range(height):
        for j in range(width):
            imgArray[i, j] = 
