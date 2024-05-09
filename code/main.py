import os
import constants as const
from get_project_root import root_path
import helpers as h
import search as s


def main():
    dirname = root_path(ignore_cwd=True)
    filename = os.path.join(dirname, 'levels/simple.txt')
    levels = h.parse_level(filename)

    for i in range(len(levels)):
        for m in const.SEARCH:
            print(s.search(levels[i], m), "Level: " + str(i) + " ,Mode: " + str(m))
        print(s.idfs(levels[i]), "Level: " + str(i) + " ,Mode: " + "idfs")

        for heu in const.HEURISTICS:
            print(s.a_star(levels[i], const.heu_mapping(heu)), "Level: " + str(i) + " ,Heuristic: " + str(heu))
            print(s.ida_star(levels[i], const.heu_mapping(heu)), "Level: " + str(i) + " ,Heuristic: " + str(heu))


if __name__ == "__main__":
    main()
