from scipy.optimize import linear_sum_assignment

import constants as const
from coordinate import *
from sokobanState import *


def parse_level(input):
    """ Gets levels as txt file and return array of start states"""
    levels = []
    position_marking, position_border, position_player, position_boxes, position_tiles = set(), set(), None, set(), set()
    x, y = 0, 0

    f = open(input, 'r')
    lines = f.readlines()
    for line in lines:
        if line == '\n':
            x, y = -1, -1
            if position_player is not None:  # for empty lines
                levels.append(
                    SokobanState(position_marking, position_border, position_player, frozenset(position_boxes),
                                 position_tiles))
                levels[-1].is_trivial_deadlock()
                position_marking, position_border, position_player, position_boxes, position_tiles = set(), set(), None, set(), set()
        for c in line:
            if c == '#':
                position_border.add(Coordinate((x, y)))
            elif c == '.':
                position_marking.add(Coordinate((x, y)))
            elif c == '@':
                position_player = Coordinate((x, y))
                position_tiles.add(Coordinate((x, y)))
            elif c == '$':
                position_boxes.add(Coordinate((x, y)))
            elif c == '*':
                position_marking.add(Coordinate((x, y)))
                position_boxes.add(Coordinate((x, y)))
            elif c == '+':
                position_marking.add(Coordinate((x, y)))
                position_player = Coordinate((x, y))
            elif c != '\n':
                position_tiles.add(Coordinate((x, y)))
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


def pattern_db(state):  # TODO ist jedes mal neu rechen klug?
    """ flood to all markings; here stop if marking reached """
    temp = []
    for b in state.position_boxes:
        queue = [b]
        visited = set()
        depth = {b: 0}
        not_found = True
        while not_found:
            pos = queue.pop(0)
            # if box stand on marking
            if pos in state.position_markings and pos not in visited:
                not_found = False
                temp.append(depth[pos])
                break
            visited.add(pos)
            for i in const.STATES:
                if pos + i in state.position_markings:  # TODO need this ?
                    not_found = False
                    temp.append(depth[pos] + 1)
                    break
                if pos + i in state.position_border or pos + i in visited or not not_found:
                    continue
                queue.append(pos + i)
                depth[pos + i] = depth[pos] + 1

    return sum(temp)


def minimal_matching(state):  # TODO ist jedes mal neu rechen klug?
    """ flood to all markings; an find minimal matching """
    all_dicts = []
    for b in state.position_boxes:
        queue = [b]
        visited = set()
        depth = {b: 0}
        temp = {}
        while queue:
            pos = queue.pop(0)
            # if box stand on marking
            if pos in state.position_markings and pos not in visited:
                temp[pos] = depth[pos]
            visited.add(pos)
            for i in const.STATES:
                if pos + i in state.position_markings and pos + i not in visited:  # TODO need this ?
                    temp[pos + i] = depth[pos] + 1  # break ???
                if pos + i in state.position_border or pos + i in visited:
                    continue
                queue.append(pos + i)
                depth[pos + i] = depth[pos] + 1
        all_dicts.append(temp)

    # built array
    position_markings_list = list(state.position_markings)
    arr = np.zeros((len(state.position_boxes), len(state.position_markings)))
    for x in range(len(all_dicts)):  # in boxes
        for y in range(len(state.position_markings)):
            arr[x][y] = all_dicts[x][position_markings_list[y]]

    row, col = linear_sum_assignment(arr)
    tc = arr[row, col].sum()
    return tc
