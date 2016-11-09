import pyper

r = pyper.R()
r("array <- c(1, 1, 4, 5, 1, 4)")
print (r("array"))

r("name <- c('高海 千歌', '桜内 梨子', '松浦 果南')")
r("height <- c(157, 160, 162)")
r("bust <- c(82, 80, 83)")
r("x <- data.frame(NAME = name, HEIGHT = height, BUST = bust)")
print(r("x"))
