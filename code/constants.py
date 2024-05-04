from enum import Enum

from coordinate import *

STATES = [Coordinate((0, 1)), Coordinate((1, 0)), Coordinate((0, -1)), Coordinate((-1, 0))]
ZERO = Coordinate((0, 0))


def mapping(c):
    if c == STATES[0]:
        return 'd'
    if c == STATES[1]:
        return 'r'
    if c == STATES[2]:
        return 'u'
    if c == STATES[3]:
        return 'l'


class Mode(Enum):
    BFS = 0  # Mode.BFS -> 0
    DFS = 1
    IDFS = 2
