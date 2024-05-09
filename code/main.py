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


    print(s.ida_star(levels[0]))

    # TODO Pipeline


if __name__ == "__main__":
    main()
