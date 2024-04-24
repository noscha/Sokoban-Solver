class SokobanState():
    ''' Was tut das '''

    def __init__(self, positionMarking, positionBorder, positionPlayer, positionBoxes):
        self.positionMarking = positionMarking
        self.positionBorder = positionBorder
        self.positionPlayer = positionPlayer
        self.positionBoxes = positionBoxes

    def successors(self):
        ''' Was tut das '''
        #TODO i and coordinates
        for i in range(4):
            if positionPLayer + 1 is not in (positionBorder or positionBoxes):
                res.append(SokobanState(positionPLayer + 1))
            elif positionPLayer + 1 is in (positionBorder or positionBoxes) and positionPlayer + 2 is not in (positionBorder or positionBoxes) and positionPlayer + 3 is not in positionBorder: 
                res.append(SokobanState(positionMarking, positionBorder, positionPlayer + 1, positionBoxes =  positionPlayer + 2))
        return res

    def is_goal(self):
        ''' Was tut das '''
        return set(positionBoxes) == set(positionMarking)
