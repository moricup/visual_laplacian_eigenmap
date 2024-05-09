from dataclasses import dataclass

from src.knot.core import Sampler
from src.knot.trefoil import TrefoilSampler
from src.knot.eight import EightSampler
from src.knot.hoph import HophSampler
from src.knot.hooph import HoophSampler
from src.knot.random_trefoil import RandomTrefoilSampler

@dataclass
class BaseKnot:
    knot_kind: str
    sample_size: int
    n_neighbors: int
    elev: int
    azim: int
    sampler_class: Sampler

TREFOIL = BaseKnot(
    knot_kind="trefoil",
    sample_size=1000,
    n_neighbors=10,
    elev=90,
    azim=0,
    sampler_class=TrefoilSampler
)

EIGHT = BaseKnot(
    knot_kind="eight",
    sample_size=1000,
    n_neighbors=10,
    elev=90,
    azim=0,
    sampler_class=EightSampler
)

HOPH = BaseKnot(
    knot_kind="hoph",
    sample_size=1000,
    n_neighbors=10,
    elev=45,
    azim=0,
    sampler_class=HophSampler
)

HOOPH = BaseKnot(
    knot_kind="hooph",
    sample_size=999,
    n_neighbors=10,
    elev=45,
    azim=0,
    sampler_class=HoophSampler
)

RANDOM_TREFOIL = BaseKnot(
    knot_kind="random_trefoil",
    sample_size=5000,
    n_neighbors=5,
    elev=60,
    azim=75,
    sampler_class=RandomTrefoilSampler
)


KNOTS = [TREFOIL, EIGHT, HOPH, HOOPH, RANDOM_TREFOIL]

