import pygame


class BasePuzzle:
    def __init__(self):
        self.vectors = [(pygame.Vector2(5, -2))]
        self.vectors_next = []
        self.index = 0

    def update(self, available_cells, obstacles):
        if all(
            [
                vector in available_cells
                and vector not in sum(obstacles, [])
                for vector in self.vectors_next
            ]
        ):
            self.index += 1
            if self.index >= len(self.vectors_dic):
                self.index = 0
            self.refresh()

    def refresh(self):
        self.vectors = [
            self.vectors[0] + vector for vector in self.vectors_dic[self.index]
        ]
        try:
            self.vectors_next = [
                self.vectors[0] + vector for vector in self.vectors_dic[self.index + 1]
            ]
        except Exception:
            self.vectors_next = [
                self.vectors[0] + vector for vector in self.vectors_dic[0]
            ]


class Puzzle_T(BasePuzzle):
    def __init__(self):
        super().__init__()
        self.vectors_dic = {
            0: [(0, 0), (-1, 1), (0, 1), (1, 1)],
            1: [(0, 0), (1, -1), (1, 0), (1, 1)],
            2: [(0, 0), (-1, 0), (0, 1), (1, 0)],
            3: [(0, 0), (-1, -1), (-1, 0), (-1, 1)],
        }
        self.color = (255, 0, 0)
        self.refresh()


class Puzzle_O(BasePuzzle):
    def __init__(self):
        super().__init__()
        self.vectors_dic = {0: [(0, 0), (0, -1), (1, 0), (1, -1)]}
        self.color = (0, 0, 255)
        self.refresh()


class Puzzle_S(BasePuzzle):
    def __init__(self):
        super().__init__()
        self.vectors_dic = {
            0: [(0, 0), (-1, 1), (0, 1), (1, 0)],
            1: [(0, 0), (-1, -1), (-1, 0), (0, 1)],
        }
        self.color = (0, 255, 0)
        self.refresh()


class Puzzle_Z(BasePuzzle):
    def __init__(self):
        super().__init__()
        self.vectors_dic = {
            0: [(0, 0), (-1, 0), (0, 1), (1, 1)],
            1: [(0, 0), (0, -1), (-1, 0), (-1, 1)],
        }
        self.color = (255, 0, 255)
        self.refresh()


class Puzzle_I(BasePuzzle):
    def __init__(self):
        super().__init__()
        self.vectors_dic = {
            0: [(0, 0), (-1, 0), (1, 0), (2, 0)],
            1: [(0, 0), (0, -1), (0, -2), (0, -3)],
        }
        self.color = (180, 180, 20)
        self.refresh()


class Puzzle_L(BasePuzzle):
    def __init__(self):
        super().__init__()
        self.vectors_dic = {
            0: [(0, 0), (0, -2), (0, -1), (1, 0)],
            1: [(0, 0), (0, -1), (1, -1), (2, -1)],
            2: [(0, 0), (-1, -2), (0, -1), (0, -2)],
            3: [(0, 0), (1, -1), (1, 0), (-1, 0)],
        }
        self.color = (20, 180, 180)
        self.refresh()


class Puzzle_J(BasePuzzle):
    def __init__(self):
        super().__init__()
        self.vectors_dic = {
            0: [(0, 0), (0, -2), (0, -1), (-1, 0)],
            1: [(0, 0), (0, -1), (-1, -1), (-2, -1)],
            2: [(0, 0), (1, -2), (0, -1), (0, -2)],
            3: [(0, 0), (-1, -1), (1, 0), (-1, 0)],
        }
        self.color = (180, 20, 180)
        self.refresh()
