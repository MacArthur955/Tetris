import itertools

from constants import BLUE, EMERLAND, GREEN, PINK, PURPLE, RED, YELLOW


class BasePuzzle:
    locus: list[tuple[int, int]]
    next_locus: list[tuple[int, int]]
    available_formations: list[list[tuple[int, int]]]
    formations: itertools.cycle
    current_formation: list[tuple[int, int]]
    next_formation: list[tuple[int, int]]
    color: tuple[int, int, int]

    def __init_subclass__(cls, **kwargs):
        cls.reset()

    @classmethod
    def regroup(cls):
        column, row = cls.locus[0]
        cls.locus = [(column + x, row + y) for x, y in cls.current_formation]
        cls.next_locus = [(column + x, row + y) for x, y in cls.next_formation]

    @classmethod
    def change_formation(cls, available_matrix: set):
        if available_matrix >= set(cls.next_locus):
            cls.current_formation = cls.next_formation
            cls.next_formation = next(cls.formations)
            cls.regroup()

    @classmethod
    def move(cls, direction: tuple[int, int], available_matrix: set):
        column, row = direction
        if available_matrix >= {(column + x, row + y) for x, y in cls.locus}:
            x, y = cls.locus[0]
            cls.locus[0] = (column + x, row + y)
            cls.regroup()
            return True
        return False

    @classmethod
    def reset(cls):
        cls.locus = [(5, -2)]
        cls.formations = itertools.cycle(cls.available_formations)
        cls.current_formation = next(cls.formations)
        cls.next_formation = next(cls.formations)
        cls.regroup()


class T(BasePuzzle):
    available_formations = [
        [(0, 0), (-1, 1), (0, 1), (1, 1)],
        [(0, 0), (1, -1), (1, 0), (1, 1)],
        [(0, 0), (-1, 0), (0, 1), (1, 0)],
        [(0, 0), (-1, -1), (-1, 0), (-1, 1)],
    ]
    color = RED


class O(BasePuzzle):
    available_formations = [[(0, 0), (0, -1), (1, 0), (1, -1)]]
    color = BLUE


class S(BasePuzzle):
    available_formations = [
        [(0, 0), (-1, 1), (0, 1), (1, 0)],
        [(0, 0), (-1, -1), (-1, 0), (0, 1)],
    ]
    color = GREEN


class Z(BasePuzzle):
    available_formations = [
        [(0, 0), (-1, 0), (0, 1), (1, 1)],
        [(0, 0), (0, -1), (-1, 0), (-1, 1)],
    ]
    color = PINK


class I(BasePuzzle):
    available_formations = [
        [(0, 0), (-1, 0), (1, 0), (2, 0)],
        [(0, 0), (0, -1), (0, -2), (0, -3)],
    ]
    color = YELLOW


class L(BasePuzzle):
    available_formations = [
        [(0, 0), (0, -2), (0, -1), (1, 0)],
        [(0, 0), (0, -1), (1, -1), (2, -1)],
        [(0, 0), (-1, -2), (0, -1), (0, -2)],
        [(0, 0), (1, -1), (1, 0), (-1, 0)],
    ]
    color = EMERLAND


class J(BasePuzzle):
    available_formations = [
        [(0, 0), (0, -2), (0, -1), (-1, 0)],
        [(0, 0), (0, -1), (-1, -1), (-2, -1)],
        [(0, 0), (1, -2), (0, -1), (0, -2)],
        [(0, 0), (-1, -1), (1, 0), (-1, 0)],
    ]
    color = PURPLE
