import random
from collections import defaultdict

import pygame

from constants import BLACK, DARK_GRAY, DOWN
from models import puzzle_i, puzzle_j, puzzle_l, puzzle_o, puzzle_s, puzzle_t, puzzle_z
from settings import CELL_SIZE, COLUMS_NUMBER, ROWS_NUMBER


class GameEngine:
    def __init__(self):
        self.screen = pygame.display.set_mode(
            size=(COLUMS_NUMBER * CELL_SIZE, ROWS_NUMBER * CELL_SIZE)
        )
        self.puzzles = [puzzle_t, puzzle_i, puzzle_j, puzzle_l, puzzle_o, puzzle_z, puzzle_s]
        self.puzzle = random.choice(self.puzzles)
        self.__matrix: set[tuple[int, int]] = {
            (x, y) for x in range(COLUMS_NUMBER) for y in range(-5, ROWS_NUMBER)
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
            self.puzzle = random.choice(self.puzzles)
            return False
        else:
            self.__obstacles = defaultdict(lambda: set())
            self.puzzle.reset()
            self.puzzle = random.choice(self.puzzles)
            return None

    def draw_puzzles(self):
        for x, y in self.puzzle.locus:
            rect = (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(surface=self.screen, color=self.puzzle.color, rect=rect)
            pygame.draw.rect(surface=self.screen, color=BLACK, rect=rect, width=1)

    def draw_obstacles(self):
        for x, y in self.obstacles:
            rect = (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(self.screen, DARK_GRAY, rect)
            pygame.draw.rect(self.screen, BLACK, rect, 1)

    def check_rows(self):
        rows_to_delete = [
            row for row, columns in self.__obstacles.items() if len(columns) >= COLUMS_NUMBER
        ]
        for row in sorted(rows_to_delete):
            highest_row = min(self.__obstacles)
            for y in range(row, highest_row, -1):
                self.__obstacles[y] = self.__obstacles[y - 1]
            del self.__obstacles[highest_row]

    def fall_down(self):
        while self.fall():
            pass
