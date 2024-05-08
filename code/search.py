from collections import defaultdict
from queue import PriorityQueue

import constants as const
import helpers as help


def search(start, mode=const.SEARCH.BFS):  # TODO idfs
    """ Search algorythm with modes for dfs, bfs, and idfs """
    steps = 0
    current_depth = 0  # for idfs
    max_depth = 1000  # for idfs
    queue = [start]
    visited = [start]  # make set ?? and empty
    parent = {}
    while queue:
        #if current_depth > max_depth:   # for idfs
            #return -2
        pop = 0 if mode == const.SEARCH.BFS else -1
        state = queue.pop(pop)
        visited.append(state)
        steps += 1
        for i in state.successors():
            if i.is_goal():
                parent[i] = state
                # print(current_depth)  # for idfs
                print(steps)
                return help.backtrace(parent, start, i)
            if i in visited:
                continue
            parent[i] = state
            queue.append(i)
            visited.append(i)
        current_depth += 1
    return -1


def a_star(start, mode=const.A_STAR.VANILLA, heuristic=const.HEURISTICS.EUC): # TODO iterrative
    """ A* algorythm with modes for vanilla and memory-bounded """
    steps = 0
    queue = PriorityQueue()
    queue.put((heuristic(start), heuristic(start), start))  # change heuristic
    visited = [start]  # make set ?? and empty
    g_score = {start: 0}
    f_score = defaultdict(lambda: float('inf'))
    f_score[start] = heuristic(start)
    parent = {}
    n = 0
    while not queue.empty():
        n += 1
        if n == 181:
            pass
        state = queue.get()[2]
        visited.append(state)
        steps += 1
        for i in state.successors():
            if i.is_goal():
                parent[i] = state
                print(steps)
                return help.backtrace(parent, start, i)
            if i in visited:
                continue

            temp_g_score = g_score[state] + int(i.action.isupper())
            # calculate if box moved
            h = heuristic(i) if i.action.isupper() else (f_score[state] - g_score[state])
            temp_f_score = h + temp_g_score
            if temp_f_score >= f_score[i]:  # TODO brauch ich temp ? wenn nicht, kein default dict
                continue
            g_score[i] = temp_g_score  # g_score[state] + int(i.action.isupper())
            f_score[i] = temp_f_score  # h + g_score[i]
            parent[i] = state
            queue.put((f_score[i], h, i))
            visited.append(i)

    return -1
