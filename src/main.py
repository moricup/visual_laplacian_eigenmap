from src.eigenmap import eigenmap
from src.savepic import savepic2D, savepic3D
from src.config import KNOTS

def main():
    for knot in KNOTS:
        knot_kind = knot.knot_kind
        sample_size = knot.sample_size
        n_neighbors = knot.n_neighbors
        elev = knot.elev
        azim = knot.azim
        sampler = knot.sampler_class(sample_size)
        x, y, z = sampler.sample()
        savepic3D(x,y,z,f"png/original/{knot_kind}.png",elev,azim)
        mapped_xy = eigenmap(x, y, z, n_neighbors)
        savepic2D(mapped_xy[:,0],mapped_xy[:,1],f"png/mapped/{knot_kind}.png")
if __name__ == "__main__":
    main()