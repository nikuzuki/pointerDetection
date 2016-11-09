num = 1.0
i = 1.0

for j in range(30):
    print("{0:.30f}".format(num))
    i = i / 10.0
    num = num + i
