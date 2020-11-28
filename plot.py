import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


frame = pd.read_table('data.csv', ';', dtype=str)
channel_names = list()
data_channels = list()
for i in frame.columns:
    channel_names.append(i)
    data_channels.append(frame[str(i)].astype(int).tolist())
N = len(channel_names) # number of pins
n = len(data_channels[0])


show_min, show_max = -0.2, 1.2


all_axis = list()
for i in range(N):
    all_axis.append(plt.subplot(N, 1, 1 + i))
    y = data_channels[i]
    x = range(0, len(y))
    xs = np.repeat(range(len(x)), 2)
    ys = np.repeat(y, 2)
    xs = xs[1:]
    ys = ys[:-1]
    plt.title(channel_names[i], loc='left')
    plt.plot(xs, ys)
    plt.axis([0, 10, show_min, show_max])


axpos = plt.axes([0.2, 0.01, 0.65, 0.03])
spos = Slider(axpos, 'Pos', 0.1, n)


def update(val):
    pos = spos.val
    for ax in all_axis:
        ax.axis([pos, pos + 10, show_min, show_max])


spos.on_changed(update)
plt.show()
