import matplotlib.pyplot as plt
import numpy as np

def fsum(a):
    for i in range(len(a) - 1, -1, -1):
        for j in range(i):
            a[i] += a[j]

XLEFT = -111
XRIGHT = 111
NUM = 20

xdata = np.random.random([2, NUM])

xdata1 = np.linspace(XLEFT, XRIGHT, NUM)
xdata2 = xdata1
ydata1 = xdata[0, :]
ydata2 = xdata[1, :]
fsum(ydata2)

maxitem = np.max(np.append(ydata1, ydata2))
minitem = np.min(np.append(ydata1, ydata2))

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(xdata1, ydata1, 'r', xdata2, ydata2, 'b')
ax.set_xticks(np.linspace(XLEFT, XRIGHT, NUM))
ax.set_yticks(np.linspace(minitem, maxitem, NUM))

plt.show()
