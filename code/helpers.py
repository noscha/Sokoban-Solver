from sokobanState import *
from coordinate import *


def parse_level(input):
    """ Gets levels as txt file and return array of start states"""
    levels = []
    position_marking, position_border, position_player, position_boxes = set(), set(), None, set()
    x, y = 0, 0

    f = open(input, 'r')
    lines = f.readlines()
    for line in lines:
        if line == '\n':
            x, y = -1, -1
            if position_player is not None:  # for empty lines
                levels.append(
                    SokobanState(position_marking, position_border, position_player, frozenset(position_boxes)))
                position_marking, position_border, position_player, position_boxes = set(), set(), None, set()
        for c in line:  #TODO mapping in constants
            if c == '#':
                position_border.add(Coordinate((x, y)))
            elif c == '.':
                position_marking.add(Coordinate((x, y)))
            elif c == '@':
                position_player = Coordinate((x, y))
            elif c == '$':
                position_boxes.add(Coordinate((x, y)))
            elif c == '*':
                position_marking.add(Coordinate((x, y)))
                position_boxes.add(Coordinate((x, y)))
            else:
                pass
            x += 1
        x = 0
        y += 1
    return levels


def backtrace(parent, start, end):
    """ Returns solution """
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    return ''.join([i.action for i in path[::-1]])


def euclidean(state):
    res = 0
    for b in state.position_boxes:
        temp = []
        for m in state.position_marking:
            temp.append(b.d_euclidean(m))
        res += min(temp)
    return res


def manhattan(state):
    res = 0
    for b in state.position_boxes:
        temp = []
        for m in state.position_marking:
            temp.append(b.d_manhattan(m))
        res += min(temp)
    return res


def pattern_db():
    pass


def minimal_matching():
    pass
