from sokobanState import *
from coordinate import *
import scipy.optimize


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
    """ Calculate smallest euclidean distance between box and marking """
    res = 0
    for b in state.position_boxes:
        temp = []
        for m in state.position_markings:
            temp.append(b.d_euclidean(m))
        res += min(temp)
    return res


def manhattan(state):
    """ Calculate the smallest manhattan distance between box and marking """
    res = 0
    for b in state.position_boxes:
        temp = []
        for m in state.position_markings:
            temp.append(b.d_manhattan(m))
        res += min(temp)
    return res


def pattern_db(state): # TODO ist jedes mal neu rechen klug?
    """ flood to all markings; here stop if marking reached """
    temp = []
    for b in state.position_boxes:
        queue = [b]
        visited = set()
        depth = {b: 0}
        not_found = True
        while not_found:
            pos = queue.pop(0)
            visited.add(pos)
            for i in const.STATES:
                if pos + i in state.position_border or pos + i in visited or not not_found:
                    continue
                if pos + i in state.position_markings:
                    not_found = False
                    temp.append(depth[pos] + 1)
                    break
                queue.append(pos + i)
                depth[pos + i] = depth[pos] + 1

    return sum(temp)


def minimal_matching(state):
    pass
