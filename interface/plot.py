import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

from file_handling import import_recorded


def plot_data(plot_d):
    channel_names, data_channels = plot_d
    N = len(channel_names)  # number of pins
    n = len(data_channels[0])
    
    show_min, show_max = -0.2, 1.2

    all_axis = list()
    for i in range(N):
        all_axis.append(plt.subplot(N, 1, 1 + i))
        y = data_channels[i]
        xs = np.repeat(range(len(y)), 2)
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


def plot_saved_file():
    filename = 'data.csv'
    plot_d = import_recorded(filename)
    plot_data(plot_d)


if __name__ == '__main__':
    plot_saved_file()
