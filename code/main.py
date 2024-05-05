import os

from get_project_root import root_path

import helpers as h
import search as s


def main():
    dirname = root_path(ignore_cwd=True)
    filename = os.path.join(dirname, 'levels/deleteMe.txt')
    levels = h.parse_level(filename)
    print(s.search(levels[0]))  # dfs:406   bfs:544
    print(s.a_star(levels[0]))  # euc:541   man:520   pd:566   mm:xxx

if __name__ == "__main__":
    main()
