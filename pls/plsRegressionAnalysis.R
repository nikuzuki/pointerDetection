# python側で生成したデータセットからpls回帰分析
library(pls)

# データセットの読み込み
#hs.data <- read.csv("~/graduateStudy/pyper/HS.txt")
hs.data <- read.table("~/graduateStudy/pyper/HS.txt", header = T)

# print(hs.data)
hs.plsr <- plsr(S ~ H, 1, data = hs.data, validation = "CV")
summary(hs.plsr)
plot(hs.plsr, "validation")

print(hs.plsr$coefficients)
a = hs.plsr$coefficients

hs.func <- function(x) a * x

plot(hs.data)
par(new=T)
#plot(hs.func)
