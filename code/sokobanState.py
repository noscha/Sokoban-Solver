import constants as const


class SokobanState:
    """ Class for sokoban states """

    def __init__(self, position_markings, position_border, position_player, position_boxes, position_tiles, action='s'):
        self.position_markings = position_markings
        self.position_border = position_border
        self.position_player = position_player
        self.position_boxes = position_boxes
        self.position_tiles = position_tiles
        self.action = action

    def successors(self):
        """ returns possible successor states """
        res = []
        for i in const.STATES:
            # step with no box in front
            if self.position_player + i not in self.position_border.union(self.position_boxes):

                res.append(SokobanState(self.position_markings, self.position_border,
                                        self.position_player + i, self.position_boxes,
                                        self.position_tiles, const.mapping(i)))
            # step with box in front
            elif self.position_player + i in self.position_boxes and self.position_player + (
                    i * 2) not in self.position_border.union(self.position_boxes):

                temp = set(self.position_boxes)
                temp.remove(self.position_player + i)
                if self.position_player + (i * 2) in self.position_tiles or self.is_advanced_deadlock(
                        self.position_player + (i * 2),
                        temp):
                    continue
                temp.add(self.position_player + (i * 2))
                res.append(SokobanState(self.position_markings, self.position_border,
                                        self.position_player + i, frozenset(temp),
                                        self.position_tiles, (const.mapping(i)).upper()))
        return res

    def is_goal(self):
        """ Checks if state is goal"""
        return set(self.position_boxes) == set(self.position_markings)

    def is_trivial_deadlock(self):
        deadlock = set()
        for t in self.position_tiles:

            sum = const.ZERO
            border_count = 0

            for i in const.STATES:
                if t + i in self.position_border:
                    sum += i
                    border_count += 1

            # path or no border
            if sum == const.ZERO:
                continue

            # in corner
            elif border_count >= 2:
                deadlock.add(t)
                continue

            # on border
            else:
                # if one line of box is a marking or a slope, there is no deadlock
                no_slope_or_no_marking = True
                i = t
                while i not in self.position_border:
                    if i in self.position_markings or i + sum not in self.position_border:
                        no_slope_or_no_marking = False
                        break
                    i += sum.switch()
                if not no_slope_or_no_marking:
                    continue
                i = t
                while i not in self.position_border:
                    if i in self.position_markings or i + sum not in self.position_border:
                        no_slope_or_no_marking = False
                        break
                    i += (sum.switch() * -1)

                if no_slope_or_no_marking:
                    deadlock.add(t)
                    continue

        self.position_tiles = deadlock

    def is_advanced_deadlock(self, pos, boxes):

        if len(self.position_boxes) == 1:
            return False

        border_and_box = boxes | self.position_border

        for i in const.STATES:
            # freeze deadlock
            if pos not in self.position_markings and pos + i in border_and_box and (
                    (pos + i.switch() in border_and_box and pos + (i + i.switch()) in border_and_box) or (
                    pos + (i.switch() * -1) in border_and_box and pos + (i + (i.switch() * -1)) in border_and_box)):
                return True

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
