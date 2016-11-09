# softmax function
# cording: utf-8

import sys  # argvを取得するため
import math

argvs = sys.argv
argc = len(argvs) - 1   # 先頭はファイル名なので除外

expList = []
denominator = 0.0

# 分母を計算
for i in range(argc):
    expList.append(math.exp(float(argvs[i+1])))
    denominator = denominator + expList[i]

# yベクトルを出力
for i in range(argc):
    print(expList[i] / denominator)
