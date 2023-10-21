import itertools

from constants import BLUE, EMERLAND, GREEN, PINK, PURPLE, RED, YELLOW


class BasePuzzle:
    def regroup(self):
        column, row = self.locus[0]
        self.locus = [(column + x, row + y) for x, y in self.current_formation]
        self.next_locus = [(column + x, row + y) for x, y in self.next_formation]

    def change_formation(self, available_matrix: set):
        if available_matrix >= set(self.next_locus):
            self.current_formation = self.next_formation
            self.next_formation = next(self.formations)
            self.regroup()

    def move(self, direction: tuple[int, int], available_matrix: set):
        column, row = direction
        if available_matrix >= {(column + x, row + y) for x, y in self.locus}:
            x, y = self.locus[0]
            self.locus[0] = (column + x, row + y)
            self.regroup()
            return True
        return False

    def reset(self):
        self.locus = [(5, -2)]
        self.formations = itertools.cycle(self.available_formations)
        self.current_formation = next(self.formations)
        self.next_formation = next(self.formations)
        self.regroup()


class T(BasePuzzle):
    def __init__(self):
        self.available_formations = [
            [(0, 0), (-1, 1), (0, 1), (1, 1)],
            [(0, 0), (1, -1), (1, 0), (1, 1)],
            [(0, 0), (-1, 0), (0, 1), (1, 0)],
            [(0, 0), (-1, -1), (-1, 0), (-1, 1)],
        ]
        self.color = RED
        self.reset()


class O(BasePuzzle):
    def __init__(self):
        self.available_formations = [[(0, 0), (0, -1), (1, 0), (1, -1)]]
        self.color = BLUE
        self.reset()


class S(BasePuzzle):
    def __init__(self):
        self.available_formations = [
            [(0, 0), (-1, 1), (0, 1), (1, 0)],
            [(0, 0), (-1, -1), (-1, 0), (0, 1)],
        ]
        self.color = GREEN
        self.reset()


class Z(BasePuzzle):
    def __init__(self):
        self.available_formations = [
            [(0, 0), (-1, 0), (0, 1), (1, 1)],
            [(0, 0), (0, -1), (-1, 0), (-1, 1)],
        ]
        self.color = PINK
        self.reset()


class I(BasePuzzle):
    def __init__(self):
        self.available_formations = [
            [(0, 0), (-1, 0), (1, 0), (2, 0)],
            [(0, 0), (0, -1), (0, -2), (0, -3)],
        ]
        self.color = YELLOW
        self.reset()


class L(BasePuzzle):
    def __init__(self):
        self.available_formations = [
            [(0, 0), (0, -2), (0, -1), (1, 0)],
            [(0, 0), (0, -1), (1, -1), (2, -1)],
            [(0, 0), (-1, -2), (0, -1), (0, -2)],
            [(0, 0), (1, -1), (1, 0), (-1, 0)],
        ]
        self.color = EMERLAND
        self.reset()


class J(BasePuzzle):
    def __init__(self):
        self.available_formations = [
            [(0, 0), (0, -2), (0, -1), (-1, 0)],
            [(0, 0), (0, -1), (-1, -1), (-2, -1)],
            [(0, 0), (1, -2), (0, -1), (0, -2)],
            [(0, 0), (-1, -1), (1, 0), (-1, 0)],
        ]
        self.color = PURPLE
        self.reset()
