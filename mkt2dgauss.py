import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm

fig = plt.figure()  # 新規のウィンドウを描画
ax = fig.add_subplot(111, projection='3d')  # サブプロット

x = y = np.arange(-6, 7, 1)
#print(x)
#print(y)

X, Y = np.meshgrid(x, y)
#print(X)
#print(Y)

# 平均と分散
mu = np.array([0, 0])
sigma = np.array([[10, 0], [0, 10]])

#print(mu)
#print(sigma)

# 行列式を計算
det = np.linalg.det(sigma)
#print(det)

# 逆行列を計算
inv_sigma = np.linalg.inv(sigma)
#print(inv_sigma)

# Gauss二次元確率密度を返す関数
def f(x, y):
    x_c = np.array([x, y]) - mu
    return np.exp(- x_c.dot(inv_sigma).dot(x_c[np.newaxis, :].T)/2.0) \
    / (2 * np.pi * np.sqrt(det))

# 配列それぞれに対応するものを返す関数に変える
Z = np.vectorize(f)(X, Y)
print(Z)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm)
plt.show()
print(np.sum(Z))
