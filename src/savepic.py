import matplotlib.pyplot as plt

def savepic3D(x, y, z, picname, elev, azim):
    fig = plt.figure(figsize=(9, 9), facecolor="w")
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(x, y, z)
    ax.view_init(elev = elev, azim = azim)
    plt.savefig(picname)

def savepic2D(x, y, picname):
    fig = plt.figure(figsize=(9, 9), facecolor="w")
    ax = fig.add_subplot(111)
    ax.scatter(x, y)
    plt.savefig(picname)