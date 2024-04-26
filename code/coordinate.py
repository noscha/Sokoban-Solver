class Coordinate:

    def __init__(self, t):
        """ t is tuple of form (x, y)"""
        self.coordinate = t

    def switch(self):
        return Coordinate(self.coordinate[::-1])

    def __mul__(self, other):
        return Coordinate(tuple([other * x for x in self.coordinate]))

    def __add__(self, other):
        return Coordinate(tuple(map(sum, zip(self.coordinate, other.coordinate))))

    def __eq__(self, other):
        return self.coordinate == other.coordinate

    def __hash__(self):
        return hash(self.coordinate)
