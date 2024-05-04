from queue import PriorityQueue

import helpers as h


def search(start):
    """ Was tut das """  #TODO mode
    steps = 0
    current_depth = 0  # for idfs
    max_depth = 1000  # for idfs
    queue = [start]
    visited = [start]  # make set ?? and empty
    parent = {}
    while queue:
        if current_depth > max_depth:
            return 0
        state = queue.pop(-1)  # -1 for dfs and idfs; 0 for bfs
        visited.append(state)
        steps += 1
        for i in state.successors():
            if i.is_goal():
                parent[i] = state
                print(steps)
                print(current_depth)  # for idfs
                return h.backtrace(parent, start, i)
            if i in visited:  # or in queue ?
                continue
            parent[i] = state
            queue.append(i)
            visited.append(i)
        current_depth += 1
    return -1


def a_star(start):
    """ Was tut das """
    steps = 0
    queue = PriorityQueue()
    queue.put((h.euclidean(start), start))  # change heuristic
    visited = [start]  # make set ?? and empty
    g_score = {start: 0}
    f_score = {start: h.euclidean(start)}  # change heuristic
    parent = {}

    while queue:
        state = queue.get()[1]
        visited.append(state)
        steps += 1
        for i in state.successors():
            if i.is_goal():
                parent[i] = state
                print(steps)
                return h.backtrace(parent, start, i)
            if i in visited:
                continue
            g_score[i] = g_score[state] + int(i.action.isupper())
            f_score[i] = h.euclidean(i) + g_score[i]  # change heuristic
            parent[i] = state
            queue.put((f_score[i], i))
            visited.append(i)

    return -1


def idfs():
    i = 1
    while True:
        pass
