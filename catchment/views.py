"""Module containing code for plotting inflammation data."""

from matplotlib import pyplot as plt
import numpy as np
import os 


def visualize(data_dict,a=None, b=None):
    """Display plots of basic statistical properties of the given data.

    :param data_dict: Dictionary of name -> data to plot
    """

    num_plots = len(data_dict)
    #fig = plt.figure(figsize=((3 * num_plots) + 1, 3.0))
    fig = plt.figure(figsize=((5 * num_plots) + 1, 5.0))

    for i, (name, data) in enumerate(data_dict.items()):
        axes = fig.add_subplot(1, num_plots, i + 1)

        axes.set_ylabel(name)
        axes.plot(data)
        axes.legend(data.columns)
        axes.set_xticklabels(data.index, rotation=90)
        axes.set_title(b)
        a = os.path.basename(a)[:-4]
        fname = f'{a}_{b}.png'

    fig.tight_layout()
    plt.savefig(fname)

    plt.show()