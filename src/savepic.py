import matplotlib.pyplot as plt

def savepic(x, y, picname):
    fig = plt.figure(figsize=(9, 9), facecolor="w")
    ax = fig.add_subplot(111)
    ax.scatter(x, y)
    plt.savefig(picname)