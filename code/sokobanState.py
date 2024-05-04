import constants as const


class SokobanState:
    """ Class for sokoban states """

    def __init__(self, position_marking, position_border, position_player, position_boxes, action='s'):  # TODO markings
        self.position_marking = position_marking
        self.position_border = position_border
        self.position_player = position_player
        self.position_boxes = position_boxes
        self.action = action

    def successors(self):
        """ returns possible successor states """
        res = []
        for i in const.STATES:
            if self.is_trivial_deadlock():
                continue
            # step with no box in front
            elif self.position_player + i not in self.position_border.union(self.position_boxes):

                res.append(SokobanState(self.position_marking, self.position_border,
                                        self.position_player + i, self.position_boxes,
                                        const.mapping(i)))
            # step with box in front
            elif self.position_player + i in self.position_boxes and self.position_player + (
                    i * 2) not in self.position_border.union(self.position_boxes):

                temp = set(self.position_boxes)  # TODO copy or not
                temp.remove(self.position_player + i)
                temp.add(self.position_player + (i * 2))

                res.append(SokobanState(self.position_marking, self.position_border,
                                        self.position_player + i, frozenset(temp),
                                        (const.mapping(i)).upper()))
        return res

    def is_goal(self):
        """ Checks if state is goal"""
        return set(self.position_boxes) == set(self.position_marking)

    def is_trivial_deadlock(self):  # TODO aufruf bei box veschiebung und nur für diese kiste
        """ Detects deadlock wich depend one one box"""
        sum = const.ZERO
        border_count = 0
        for b in self.position_boxes:
            for i in const.STATES:
                if b + i in self.position_border:
                    sum += i
                    border_count += 1
            # no border or a path
            if sum == const.ZERO:
                continue

            # in corner
            elif border_count > 2:
                return not (b in self.position_marking)

            # on border
            else:  #TODO make better
                no_marking = True
                i = b
                while i not in self.position_border:
                    if i in self.position_marking:
                        no_marking = False
                        break
                    i += sum.switch()
                if not no_marking:
                    break
                i = b
                while i not in self.position_border:
                    if i in self.position_marking:
                        no_marking = False
                        break
                    i += (sum.switch() * -1)
                if no_marking:
                    return True

        return False

    def __eq__(self, other):
        return (self.position_player, self.position_boxes) == (other.position_player, other.position_boxes)

    def __str__(self):
        return str(self.action)

    def __hash__(self):
        return hash((self.position_player, self.position_boxes))

    def __lt__(self, other):
        return id(self) < id(other)

    def __le__(self, other):
        return id(self) <= id(other)
