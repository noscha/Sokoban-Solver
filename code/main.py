import helpers as h
import search as s
import os
from get_project_root import root_path


def main():
    dirname = root_path(ignore_cwd=True)
    filename = os.path.join(dirname, 'levels/deleteMe.txt')
    levels = h.parse_level(filename)
    print(s.search(levels[0]))


if __name__ == "__main__":
    main()
