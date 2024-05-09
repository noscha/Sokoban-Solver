import os
import constants as const
from pathlib import Path
import helpers as h
import search as s


def main():
    dirname = Path(__file__).parent.parent
    filename = os.path.join(dirname, 'levels/simple.txt')
    levels = h.parse_level(filename)

    for i in range(len(levels)):
        for m in const.SEARCH:
            print(s.search(levels[i], m), "Level: " + str(i) + " ,Mode: " + str(m))
        print(s.idfs(levels[i]), "Level: " + str(i) + " ,Mode: " + "idfs")

        for heu in const.HEURISTICS:
            print(s.a_star(levels[i], const.heu_mapping(heu)), "Level: " + str(i) + " ,Heuristic: " + str(heu) + " ,Mode: " + "vanilla")
            print(s.ida_star(levels[i], const.heu_mapping(heu)), "Level: " + str(i) + " ,Heuristic: " + str(heu) + " ,Mode: " + "ida*")


if __name__ == "__main__":
    main()
