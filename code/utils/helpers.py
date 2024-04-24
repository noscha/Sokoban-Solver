def parse_level(input):
        ''' Was tut das '''
        levels = []
        positionMarking, positionBorder, positionPlayer, positionBoxes = set(), set(), None, set()
        x, y = 0, 0

        f = open(input, 'r')
        lines = file1.readlines()
        for line in lines:
            if line == '\n':
                x, y = -1, -1
                levels.append(SokobanState(positionMarking, positionBorder, positionPlayer, positionBoxes))
                positionMarking, positionBorder, positionPlayer, positionBoxes = set(), set(), None, set()
            for c in line:
                if c == '#':
                    positionBorder.add((x, y))
                elif c == '.':
                    positionMarking.add((x, y))
                elif c == '@':
                    positionPLayer = (x, y)
                elif c == '$':
                    positionBoxes.add((x, y))
                else:
                    pass
                x += 1
            y += 1
        return levels
