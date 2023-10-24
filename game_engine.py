import random
from collections import defaultdict
from typing import Iterable

import pygame

from constants import BLACK, DOWN
from models import puzzles
from settings import CELL_SIZE, COLUMNS_NUMBER, ROWS_NUMBER


class GameEngine:
    def __init__(self):
        self.puzzle = random.choice(puzzles)
        self.__matrix: set[tuple[int, int]] = {
            (x, y) for x in range(COLUMNS_NUMBER) for y in range(-5, ROWS_NUMBER)
        }
        self.__obstacles: defaultdict = defaultdict(lambda: set())

    @property
    def obstacles(self):
        return {(x, y) for y in self.__obstacles.keys() for x in self.__obstacles[y]}

    @property
    def available_matrix(self) -> set:
        return self.__matrix - self.obstacles

    def fall(self):
        if self.puzzle.move(DOWN, self.available_matrix):
            return True
        elif self.obstacles.isdisjoint(self.puzzle.locus):
            for x, y in self.puzzle.locus:
                self.__obstacles[y].add(x)
            self.check_rows()
            self.puzzle.reset()
            self.puzzle = random.choice(puzzles)
            return False
        else:
            self.__obstacles = defaultdict(lambda: set())
            self.puzzle.reset()
            self.puzzle = random.choice(puzzles)
            return None

    @staticmethod
    def draw_blocks(screen: pygame, color: tuple[int, int, int], blocks: Iterable):
        for x, y in blocks:
            rect = (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, BLACK, rect, 1)

    def check_rows(self):
        rows_to_delete = [
            row for row, columns in self.__obstacles.items() if len(columns) >= COLUMNS_NUMBER
        ]
        for row in sorted(rows_to_delete):
            highest_row = min(self.__obstacles)
            for y in range(row, highest_row, -1):
                self.__obstacles[y] = self.__obstacles[y - 1]
            del self.__obstacles[highest_row]

    def fall_down(self):
        while self.fall():
            pass
