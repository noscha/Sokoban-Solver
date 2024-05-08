import os
import constants as const  # do not remove
from get_project_root import root_path
import helpers as h
import search as s
from coordinate import *


def main():

    dirname = root_path(ignore_cwd=True)
    filename = os.path.join(dirname, 'levels/simple.txt')
    levels = h.parse_level(filename)

    n = 0
    for i in levels:
        print(s.a_star(i), n)
        n += 1


if __name__ == "__main__":
    main()
