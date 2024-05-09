from collections import defaultdict
from queue import PriorityQueue

import constants as const
import helpers as help


def search(start, mode=const.SEARCH.BFS, max_depth=float('inf')):
    """ Search algorythm with modes for dfs, bfs, and idfs """
    # for idfs
    current_depth = 0

    steps = 0
    queue = [start]
    visited = [start]  # make set ?? and empty
    parent = {}
    while queue:
        pop = 0 if mode == const.SEARCH.BFS else -1
        state = queue.pop(pop)
        visited.append(state)
        steps += 1
        current_depth += 1

        # for idfs
        if current_depth >= max_depth:
            if not queue:
                return -1, steps
            state = queue.pop(pop)
            current_depth -= 1

        for i in state.successors():
            if i.is_goal():
                parent[i] = state
                return help.backtrace(parent, start, i), steps
            if i in visited:
                continue
            parent[i] = state
            queue.append(i)
            visited.append(i)
    return -1, steps


def idfs(start):
    """ DFS with iterative deepening """
    max_depth = 100
    steps = 0
    while 1:
        res = search(start, const.SEARCH.IDFS, max_depth)
        steps += res[1]
        if res[0] != -1:
            return res[0], steps
        max_depth += 100


def a_star(start, mode=const.A_STAR.VANILLA, heuristic=const.HEURISTICS.EUC):  # TODO iterrative
    """ A* algorythm with modes for vanilla and memory-bounded """
    steps = 0
    queue = PriorityQueue()
    queue.put((heuristic(start), heuristic(start), start))
    visited = [start]  # make set ?? and empty
    g_score = {start: 0}
    f_score = defaultdict(lambda: float('inf'))
    f_score[start] = heuristic(start)
    parent = {}
    while not queue.empty():
        state = queue.get()[2]
        visited.append(state)
        steps += 1
        for i in state.successors():
            if i.is_goal():
                parent[i] = state
                return help.backtrace(parent, start, i), steps
            if i in visited:
                continue

            temp_g_score = g_score[state] + int(i.action.isupper())
            # calculate, if box moved
            h = heuristic(i) if i.action.isupper() else (f_score[state] - g_score[state])
            temp_f_score = h + temp_g_score
            if temp_f_score >= f_score[i]:
                continue
            g_score[i] = temp_g_score
            f_score[i] = temp_f_score
            parent[i] = state
            queue.put((f_score[i], h, i))
            visited.append(i)

    return -1


def ia_star(start, heuristic=const.HEURISTICS.EUC):
    """ A* with iterative deepening """
    max_limit_next, res = heuristic(start), -1
    while res != -1 and max_limit_next != float('inf'):  # res???
        max_limit, max_limit_next = max_limit_next, float('inf')
        res, max_limit_next = a_star(start, const.A_STAR.IA, heuristic)
    return res
