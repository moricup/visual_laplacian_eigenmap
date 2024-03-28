import matplotlib.pyplot as plt
import numpy as np

def savepic3D(x, y, z, picname, elev, azim):
    fig = plt.figure(figsize=(9, 9), facecolor="w")
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(x, y, z, c = np.linspace(start=0.0, stop = 1.0, num = len(x)), cmap="hsv")
    ax.view_init(elev = elev, azim = azim)
    plt.savefig(picname)

def savepic2D(x, y, picname):
    fig = plt.figure(figsize=(9, 9), facecolor="w")
    ax = fig.add_subplot(111)
    ax.scatter(x, y, c = np.linspace(start=0.0, stop = 1.0, num = len(x)), cmap="hsv")
    plt.savefig(picname)