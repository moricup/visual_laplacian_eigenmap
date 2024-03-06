import json

from src.knot.trefoil import TrefoilSampler
from src.eigenmap import eigenmap
from src.savepic import savepic


def main():
    with open("config.json") as f:
        config = json.load(f)
    sample_size = config["sample_size"]
    knots = config["knots"]

    for knot in knots:
        if knot == "trefoil":
            sampler = TrefoilSampler(sample_size)
        else:
            raise ValueError(f"Unknown knot: {knot}")
        x, y, z = sampler.sample()
        mapped_xy = eigenmap(x, y, z)
        savepic(mapped_xy[:, 0], mapped_xy[:, 1], f"png/mapped/{knot}.png")

if __name__ == "__main__":
    main()