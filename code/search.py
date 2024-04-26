import helpers as h


def search(start):
    """ Was tut das """  #TODO mode
    steps = 0
    queue = [start]
    visited = [start]
    parent = {}
    while queue:
        state = queue.pop(0) # -1 for dfs
        steps += 1
        visited.append(state)
        for i in state.successors():
            if i.is_goal():
                parent[i] = state
                print(steps)
                return h.backtrace(parent, start, i)
            if i in visited:
                continue
            parent[i] = state
            queue.append(i)
            visited.append(i)

    return -1


def idfs(state):
    current_depth = 0
    max_depth = 1
    pass
