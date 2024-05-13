import time
from collections import defaultdict
from queue import PriorityQueue

import constants as const
import helpers as help


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
                path = help.backtrace(parent, start, i)
                return steps, steps ** (1 / len(path)), time.process_time() - t, path
            if i in visited:
                continue
            parent[i] = state
            queue.append(i)
            visited.add(i)

    return steps, 0, time.process_time() - t, -1


def idfs(start):
    """ DFS with iterative deepening """
    t = time.process_time()
    max_depth = 100
    steps = 0
    while 1:  # assume no unsolvable levels
        res = search(start, const.SEARCH.DFS, max_depth)
        steps += res[0]
        path = res[3]
        if path != -1:
            return steps, steps ** (1 / len(path)), time.process_time() - t, path
        max_depth += 100


def a_star(start, heuristic=const.heu_mapping(const.HEURISTICS.EUC)):
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

        for i in state.successors():
            if i.is_goal():
                parent[i] = state
                path = help.backtrace(parent, start, i)
                return steps, steps ** (1 / len(path)), time.process_time() - t, path
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

    return steps, 0, time.process_time() - t, float('inf'), -1


def ida_star(start, heuristic=const.heu_mapping(const.HEURISTICS.EUC)):
    """ A* with iterative deepening """

    if start.is_goal():
        return 0, 0, 0, "finished"

    t = time.process_time()
    steps = 0
    next_limit = heuristic(start)

    while next_limit != float('inf'):
        limit = next_limit
        next_limit = float('inf')
        queue = [start]
        visited = set()
        parents = {}
        g_score = {start: 0}

        while queue:
            state = queue.pop(-1)
            visited.add(state)
            steps += 1

            for next_state in state.successors():
                if next_state.is_goal():
                    parents[next_state] = state
                    path = help.backtrace(parents, start, next_state)
                    return steps, steps ** (1 / len(path)), time.process_time() - t, path

                if next_state in visited:
                    continue

                predecessor = state
                g_score[next_state] = g_score[predecessor] + int(next_state.action.isupper())
                f_score = heuristic(next_state) + g_score[next_state]
                if f_score > limit:
                    if f_score < next_limit:
                        next_limit = f_score
                else:
                    parents[next_state] = state
                    queue.append(next_state)

    return steps, 0, time.process_time() - t, -1
