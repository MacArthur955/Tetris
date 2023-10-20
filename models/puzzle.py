import pygame
from constants import RED, BLUE, GREEN, PINK, YELLOW, PURPLE, EMERLAND
import itertools


class BasePuzzle:
    def regroup(self):
        self.locus = [self.locus[0] + vector for vector in self.current_formation]
        self.next_locus = [self.locus[0] + vector for vector in self.next_formation]

    def change_formation(self, available_matrix: set):
        if all(vector in list(available_matrix) for vector in self.next_locus):
            self.current_formation = self.next_formation
            self.next_formation = next(self.formations)
            self.regroup()

    def move(self, direction: tuple[int, int], available_matrix: set):
        if all(block + direction in list(available_matrix) for block in self.locus):
            self.locus[0] += direction
            self.regroup()
            return True
        return False

    def reset(self):
        self.locus = [(pygame.Vector2(5, -2))]
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
