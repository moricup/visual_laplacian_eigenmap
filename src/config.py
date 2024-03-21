from dataclasses import dataclass

from src.knot.core import Sampler
from src.knot.trefoil import TrefoilSampler
from src.knot.hoph import HophSampler

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

HOPH = BaseKnot(
    knot_kind="hoph",
    sample_size=1000,
    n_neighbors=10,
    elev=45,
    azim=0,
    sampler_class=HophSampler
)

KNOTS = [TREFOIL, HOPH]
