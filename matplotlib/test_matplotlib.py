import matplotlib.pyplot as plt
import numpy as np

def fsum(a):
    for i in range(len(a) - 1, -1, -1):
        for j in range(i):
            a[i] += a[j]

XLEFT = -111
XRIGHT = 111
NUM = 20

data = np.random.random(NUM)

xdata1 = np.linspace(XLEFT, XRIGHT, NUM)
xdata2 = xdata1
ydata1 = data - 0.5
ydata2 = ydata1.copy()
fsum(ydata2)

maxitem = np.max(np.append(ydata1, ydata2))
minitem = np.min(np.append(ydata1, ydata2))

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(xdata1, ydata1, 'r', xdata2, ydata2, 'b')
fig.tight_layout()

plt.show()
