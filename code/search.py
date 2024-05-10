import time
from collections import defaultdict
from queue import PriorityQueue

import constants as const
import helpers as help
import time


def search(start, mode=const.SEARCH.BFS, max_depth=float('inf')):
    """ Search algorythm with modes for dfs, bfs, and idfs """
    t = time.process_time()

    # for idfs
    current_depth = 0

    steps = 0
    queue = [start]
    visited = set()
    parent = {}
    while queue:
        pop = 0 if mode == const.SEARCH.BFS else -1
        state = queue.pop(pop)
        visited.add(state)
        steps += 1
        current_depth += 1

        # for idfs
        if current_depth >= max_depth:
            current_depth -= 1
            continue

        for i in state.successors():
            if i.is_goal():
                parent[i] = state
                return help.backtrace(parent, start, i), steps, time.process_time() - t
            if i in visited:
                continue
            parent[i] = state
            queue.append(i)
            visited.add(i)

    return -1, steps, -1


def idfs(start):
    """ DFS with iterative deepening """
    t = time.process_time()
    max_depth = 100
    steps = 0
    while 1:  # assume no unsolvable levels
        res = search(start, const.SEARCH.DFS, max_depth)
        steps += res[1]
        if res[0] != -1:
            return res[0], steps, time.process_time() - t
        max_depth += 100


def a_star(start, heuristic=const.heu_mapping(const.HEURISTICS.EUC), mode=const.A_STAR.VANILLA, max_limit=float('inf')):
    """ A* algorythm with modes for vanilla and memory-bounded """
    t = time.process_time()
    steps = 0
    queue = PriorityQueue()
    queue.put((heuristic(start), heuristic(start), start))
    visited = set()
    g_score = {start: 0}
    f_score = defaultdict(lambda: float('inf'))
    f_score[start] = heuristic(start)
    parent = {}
    while not queue.empty():
        state = queue.get()[2]
        visited.add(state)
        steps += 1

        # for ida
        if g_score[state] > max_limit:
            return -1, steps, g_score[state], -1

        for i in state.successors():
            if i.is_goal():
                parent[i] = state
                return (help.backtrace(parent, start, i), steps, -1, -1) if mode == const.A_STAR.IDA else (help.backtrace(parent, start, i), steps, time.process_time() - t)
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
            visited.add(i)

    return -1, steps, float('inf'), -1


def ida_star(start, heuristic=const.heu_mapping(const.HEURISTICS.EUC)):
    """ A* with iterative deepening, with visited """
    t = time.process_time()
    max_limit = heuristic(start)
    steps = 0

    while 1:  # assume no unsolvable levels
        res, temp_steps, max_limit, trash = a_star(start, heuristic, const.A_STAR.IDA, max_limit)
        steps += temp_steps
        if res != -1:
            return res, steps, time.process_time() - t
