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


# a*
class A_STAR(Enum):
    VANILLA = "vanilla"
    IDA = "ida"


class HEURISTICS(Enum):
    EUC = "euc"
    MAN = "man"
    PDB = "pdb"
    MM = "mm"


def heu_mapping(heu):
    if heu == HEURISTICS.EUC:
        return help.euclidean
    elif heu == HEURISTICS.MAN:
        return help.manhattan
    elif heu == HEURISTICS.PDB:
        return help.pattern_db
    elif heu == HEURISTICS.MM:
        return help.minimal_matching


def mapping(c):
    if c == STATES[0]:
        return 'd'
    elif c == STATES[1]:
        return 'r'
    elif c == STATES[2]:
        return 'u'
    elif c == STATES[3]:
        return 'l'
