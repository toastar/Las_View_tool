#!/usr/bin/python

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
x=np.arange(100.)
y=np.sin(x)

#subplots(nrows=1, ncols=1, sharex=False, sharey=False, squeeze=True, subplot_kw=None, **fig_kw)
plt.subplot(311)

plt.plot(x,y)
plt.subplot(312)

plt.scatter(x,y)

plt.subplot(313)

labels=[" %d"%i for i in range(len(x))]

#for i in range(len(x)):
#    labels[i]="%d"%i

for i in range(len(x)):
    plt.annotate(labels[i],xy=(x[i],y[i]),ha="left",va="center")

plt.scatter(x,y)
plt.show()


