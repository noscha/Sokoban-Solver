from enum import Enum

import helpers as help
from coordinate import *

# coordinates
STATES = [Coordinate((0, 1)), Coordinate((1, 0)), Coordinate((0, -1)), Coordinate((-1, 0))]
ZERO = Coordinate((0, 0))


# search
class SEARCH(Enum):
    BFS = "bfs"
    DFS = "dfs"
    IDFS = "idfs"


# a*
class A_STAR(Enum):
    VANILLA = "vanilla"
    IDA = "ida"


class HEURISTICS(Enum):
    EUC = help.euclidean
    MAN = help.manhattan
    PDB = help.pattern_db
    MM = help.minimal_matching


class DEADLOCKS(Enum):
    TRIVIAL = "trivial"
    ADVANCED = "iter"


def mapping(c):
    if c == STATES[0]:
        return 'd'
    if c == STATES[1]:
        return 'r'
    if c == STATES[2]:
        return 'u'
    if c == STATES[3]:
        return 'l'
