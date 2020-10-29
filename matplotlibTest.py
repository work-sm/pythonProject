import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

fig = plt.figure()
ax = fig.add_subplot(111, xlim=(0, 10), ylim=(-4, 4))
sx = 0
sy = 0
r = 1.5
circle = mpatches.Circle((sx, sy), r, ec='b', fc='b', alpha=0.6)
ax.add_patch(circle)
n = 5
alpha = np.linspace(-np.pi / 2, np.pi / 2, 100)
for i in range(1, n + 1):
    a = (i + 1) * 2
    b = (i + 1)
    plt.plot(a * np.cos(alpha), b * np.sin(alpha))
    if i <= 3:
        ax.text(a + 1, 0, 'layer.%d' % (i - 1), ha='center', va='center')
rate = 3
Jnum = 100
for i in range(Jnum):
    data = stats.poisson.rvs(mu=rate, loc=0, size=1)
    while data == 0:
        data = stats.poisson.rvs(mu=rate, loc=0, size=1)
    data = data[0]
    r = np.random.random()
    beta = (np.random.random() - 0.5) * np.pi
    print(beta)
    data += r
    a = (data + 1) * 2 * np.cos(beta)
    b = (data + 1) * np.sin(beta)
    ax.scatter(a, b, c='y', edgecolors='y')
xx = [3.5, 6.8, 6.8]
yy = [-1.8, 0.9, 3.1]
pp = [1.00, 0.85, 0.75]
rota = [-45, 0, 0]
for i in range(3):
    plt.plot((1.5, xx[i]), (0, yy[i]), 'r')
    ax.scatter(xx[i], yy[i], c='y', edgecolors='b')
    ax.text(xx[i], yy[i], 'probability %lf' % pp[i], ha='center')
tx = np.linspace(0, 10, 10)
ty = np.linspace(-4, -4, 10)
ax.set_xticks(tx)
ax.set_xticklabels('')
ax.set_yticks(ty)
ax.set_yticklabels('')
# plt.axis('off')
plt.show()
