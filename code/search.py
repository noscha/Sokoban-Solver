from collections import defaultdict
from queue import PriorityQueue

import helpers as h


def search(start):
    """ Search algorythm with modes for dfs, bfs, and idfs """  #TODO mode
    steps = 0
    current_depth = 0  # for idfs
    max_depth = 1000  # for idfs
    queue = [start]
    visited = [start]  # make set ?? and empty
    parent = {}
    while queue:
        if current_depth > max_depth:
            return 0
        state = queue.pop(0)  # -1 for dfs and idfs; 0 for bfs
        visited.append(state)
        steps += 1
        for i in state.successors():
            if i.is_goal():
                parent[i] = state
                print(steps)
                #print(current_depth)  # for idfs
                return h.backtrace(parent, start, i)
            if i in visited:
                continue
            parent[i] = state
            queue.append(i)
            visited.append(i)
        current_depth += 1
    return -1


def a_star(start):  #TODO heuristic nur bei box verschiebung neu berechnen
    """ A* algorythm with modes for vanilla and memory-bounded """
    steps = 0
    queue = PriorityQueue()
    queue.put((h.minimal_matching(start), h.minimal_matching(start), start))  # change heuristic
    visited = [start]  # make set ?? and empty
    g_score = {start: 0}
    f_score = defaultdict(lambda: float('inf'))
    f_score[start] = h.minimal_matching(start)
    parent = {}

    while queue:
        state = queue.get()[2]
        visited.append(state)
        steps += 1
        for i in state.successors():
            if i.is_goal():
                parent[i] = state
                print(steps)
                return h.backtrace(parent, start, i)
            if i in visited:
                continue

            temp_g_score = g_score[state] + int(i.action.isupper())
            # calculate if box moved
            heuristic = h.minimal_matching(i) if i.action.isupper() else (f_score[state] - g_score[state])
            temp_f_score = heuristic + temp_g_score
            if temp_f_score >= f_score[i]:  #TODO brauch ich temp ? wenn nicht, kein default dict
                continue
            g_score[i] = temp_g_score  # g_score[state] + int(i.action.isupper())
            f_score[i] = temp_f_score  # heuristic + g_score[i]
            parent[i] = state
            queue.put((f_score[i], heuristic, i))
            visited.append(i)

    return -1


def idfs():
    i = 1
    while True:
        pass
