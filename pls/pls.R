# python側で生成したデータセットからpls回帰分析
# 誤検知時の画像を使って計測
library(pls)

# データセットの読み込み
#pointer.data <- read.table("~/graduateStudy/pls/ALL.txt", header = T)
#pointer.data <- read.table("~/graduateStudy/pls/RGB.txt", header = T)
#pointer.data <- read.table("~/graduateStudy/pls/HSV.txt", header = T)
pointer.data <- read.table("~/graduateStudy/pls/YCrCb.txt", header = T)



#pointer.plsr <- plsr(W ~ R+G+B+H+S+V+Y+Cr+Cb, 9, data = pointer.data, validation = "LOO")
#pointer.plsr <- plsr(W ~ R+G+B+H+S+V, 6, data = pointer.data, validation = "LOO")
#pointer.plsr <- plsr(W ~ R+G+B+Y+Cr+Cb, 6, data = pointer.data, validation = "LOO")
#pointer.plsr <- plsr(W ~ H+S+V+Y+Cr+Cb, 6, data = pointer.data, validation = "LOO")
#pointer.plsr <- plsr(W ~ R+G+B, 3, data = pointer.data, validation = "LOO")
#pointer.plsr <- plsr(W ~ H+S+V, 3, data = pointer.data, validation = "LOO")
pointer.plsr <- plsr(W ~ Y+Cr+Cb, 3, data = pointer.data, validation = "LOO")

summary(pointer.plsr)
plot(pointer.plsr,"validation")

pointer.plsr$coefficients[ , ,3] #データセットが3次元の場合

