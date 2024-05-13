import os
from pathlib import Path

import constants as const
import helpers as h
import search as s


def main():
    dirname = Path(__file__).parent.parent
    filename = os.path.join(dirname, 'levels/simple.txt')
    levels = h.parse_level(filename)

    print(" " * 53, "Steps  ef. branching     Time                   Path")
    for i in range(len(levels)):
        for m in const.SEARCH:
            print("Level: " + str(i) + " ,Mode: " + str(m) + "                           ", s.search(levels[i], m))
        print("Level: " + str(i) + " ,Mode: " + "idfs                                 ", s.idfs(levels[i]))

        for heu in const.HEURISTICS:
            print("Level: " + str(i) + " ,Heuristic: " + str(heu) + " ,Mode: " + "vanilla   ",
                  s.a_star(levels[i], const.heu_mapping(heu)))
            print("Level: " + str(i) + " ,Heuristic: " + str(heu) + " ,Mode: " + "ida*      ",
                  s.ida_star(levels[i], const.heu_mapping(heu)))


if __name__ == "__main__":
    main()
