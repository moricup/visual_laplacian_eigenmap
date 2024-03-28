import matplotlib.pyplot as plt
import numpy as np

def savepic3D(x, y, z, picname: str, elev: float, azim: float):
    fig = plt.figure(figsize=(9, 9), facecolor="w")
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(x, y, z, c = np.linspace(0.0, 1.0, len(x)), cmap="hsv")
    ax.view_init(elev = elev, azim = azim)
    plt.savefig(picname)

def savepic2D(x, y, picname: str):
    fig = plt.figure(figsize=(9, 9), facecolor="w")
    ax = fig.add_subplot(111)
    ax.scatter(x, y, c = np.linspace(0.0, 1.0, len(x)), cmap="hsv")
    plt.savefig(picname)