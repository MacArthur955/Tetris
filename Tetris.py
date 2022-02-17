import pygame, random
from pygame import *
from random import *

class Puzzles():
    def __init__(self):
        self.vectors = [(pygame.Vector2(5, -2))]
        self.vectors_next = []
        self.index = 0
    def update(self):
        if all([vector in game.all_cells and vector not in sum(game.obstacles.values(),[]) for vector in self.vectors_next]):
            self.index += 1
            if self.index >= len(self.vectors_dic): self.index = 0
            self.refresh()
    def refresh(self):
        self.vectors = [self.vectors[0] + vector for vector in self.vectors_dic[self.index]]
        try: self.vectors_next = [self.vectors[0] + vector for vector in self.vectors_dic[self.index+1]]
        except Exception: self.vectors_next = [self.vectors[0] + vector for vector in self.vectors_dic[0]]
class Puzzle_T(Puzzles):
    def __init__(self):
        super().__init__()
        self.vectors_dic = {0: [(0,0),(-1,1),(0,1),(1,1)], 1:[(0,0),(1,-1),(1,0),(1,1)], 2:[(0,0),(-1,0),(0,1),(1,0)], 3:[(0,0),(-1,-1),(-1,0),(-1,1)]}
        self.color = (255,0,0)
        self.refresh()
class Puzzle_O(Puzzles):
    def __init__(self):
        super().__init__()
        self.vectors_dic = {0:[(0,0),(0,-1),(1,0),(1,-1)]}
        self.color = (0,0,255)
        self.refresh()
class Puzzle_S(Puzzles):
    def __init__(self):
        super().__init__()
        self.vectors_dic = {0: [(0,0),(-1,1),(0,1),(1,0)], 1:[(0,0),(-1,-1),(-1,0),(0,1)]}
        self.color = (0,255,0)
        self.refresh()
class Puzzle_Z(Puzzles):
    def __init__(self):
        super().__init__()
        self.vectors_dic = {0: [(0,0),(-1,0),(0,1),(1,1)], 1:[(0,0),(0,-1),(-1,0),(-1,1)]}
        self.color = (255,0,255)
        self.refresh()
class Puzzle_I(Puzzles):
    def __init__(self):
        super().__init__()
        self.vectors_dic = {0: [(0,0),(-1,0),(1,0),(2,0)], 1:[(0,0),(0,-1),(0,-2),(0,-3)]}
        self.color = (180,180,20)
        self.refresh()
class Puzzle_L(Puzzles):
    def __init__(self):
        super().__init__()
        self.vectors_dic = {0: [(0,0),(0,-2),(0,-1),(1,0)], 1:[(0,0),(0,-1),(1,-1),(2,-1)], 2:[(0,0),(-1,-2),(0,-1),(0,-2)], 3:[(0,0),(1,-1),(1,0),(-1,0)]}
        self.color = (20,180,180)
        self.refresh()
class Puzzle_J(Puzzles):
    def __init__(self):
        super().__init__()
        self.vectors_dic = {0: [(0,0),(0,-2),(0,-1),(-1,0)], 1:[(0,0),(0,-1),(-1,-1),(-2,-1)], 2:[(0,0),(1,-2),(0,-1),(0,-2)], 3:[(0,0),(-1,-1),(1,0),(-1,0)]}
        self.color = (180,20,180)
        self.refresh()

class Manager():
    def __init__(self):
        self.puzzles = [Puzzle_T(), Puzzle_O(), Puzzle_S(), Puzzle_Z(), Puzzle_I(), Puzzle_L(), Puzzle_J()]
        self.puzzle = choice(self.puzzles)
        self.direction = pygame.Vector2(0,0)
        self.all_cells = self.download_all_cells()
        self.obstacles = dict()
        self.menu()
    def run_event(self):
        self.fall()
    def run(self):
        self.move()
    def draw(self):
        self.print_puzzle()
# Game
    def move(self):
        if self.direction and all(x + self.direction in self.all_cells and x + self.direction not in sum(self.obstacles.values(),[]) for x in self.puzzle.vectors):
            self.puzzle.vectors[0] += self.direction
            self.puzzle.refresh()
        self.direction = pygame.Vector2(0,0)
    def fall(self):
        if all(x + (0, 1) in self.all_cells and x + (0, 1) not in sum(self.obstacles.values(),[]) for x in self.puzzle.vectors):
            self.puzzle.vectors[0] += (0, 1)
            self.puzzle.refresh()
            return True
        else:
            for block in self.puzzle.vectors:
                if block.y not in self.obstacles: self.obstacles[block.y] = [block]
                else: self.obstacles[block.y].append(block)
            if any([block.y < 0 for block in sum(self.obstacles.values(),[])]):
                self.new_game()
                self.menu()
                return
            self.restart_puzzle()
            self.check_line()
            return False
    def print_puzzle(self):
        for vector in self.puzzle.vectors:
            pygame.draw.rect(screen, self.puzzle.color, (vector.x * cellSize, vector.y * cellSize, cellSize, cellSize))
            pygame.draw.rect(screen, (0,0,0), (vector.x * cellSize, vector.y * cellSize, cellSize, cellSize),1)
        for vector in sum(self.obstacles.values(),[]):
            pygame.draw.rect(screen, (170,170,170), (vector.x * cellSize, vector.y * cellSize, cellSize, cellSize))
            pygame.draw.rect(screen, (0,0,0), (vector.x * cellSize, vector.y * cellSize, cellSize, cellSize),1)
    def download_all_cells(self):
        all_cells = []
        for column in range(cell_columnNumber):
            for row in range(-5,cell_rowNumber):
                all_cells.append((column, row))
        return all_cells
    def restart_puzzle(self):
        self.puzzle.vectors[0] = pygame.Vector2(5, -2)
        self.puzzle.index = 0
        self.puzzle.refresh()
        self.puzzle = choice(self.puzzles)
    def check_line(self):
        delete_lines = [i for i in self.obstacles if len(self.obstacles[i]) > 10]
        for line in sorted(delete_lines):
            if len(self.obstacles) == 1: del(self.obstacles[line])
            else:
                for i in reversed(range(20-len(self.obstacles), int(line))):
                    self.obstacles[float(i + 1)] = self.obstacles[float(i)]
                    for x in self.obstacles[float(i + 1)]:
                        x.y += 1
                del(self.obstacles[20.0-float(len(self.obstacles))])
    def fall_down(self):
        while self.fall(): pass
    def new_game(self):
        self.obstacles = dict()
        self.puzzle = choice(self.puzzles)
        self.direction = pygame.Vector2(0, 0)
# Menu
    def menu(self):
        while True:
            clock.tick(FPS)
            screen.fill(background)
            for event in pygame.event.get():
                if event.type == QUIT: pygame.quit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN: return
            screen.blit(text_start,(55,110,200,200))
            pygame.display.update()

pygame.init()

cellSize, cell_columnNumber, cell_rowNumber = 25, 11, 20
FPS = 60
background = (200, 200, 200)

screen = pygame.display.set_mode((cell_columnNumber * cellSize, cell_rowNumber * cellSize))
clock = pygame.time.Clock()

pygame.time.set_timer(USEREVENT, 200)
game_font = pygame.font.Font("freesansbold.ttf", 18)

text_start = game_font.render('Press enter to start', True, (140,40,230))

game = Manager()

running = True
while running:
    clock.tick(FPS)
    screen.fill(background)
    game.draw()
    game.run()
    for event in pygame.event.get():
        if event.type == QUIT: running = False
        elif event.type == USEREVENT: game.run_event()
        elif event.type == KEYDOWN:
            if event.key == K_SPACE: game.fall_down()
            elif event.key == K_w or event.key == K_UP: game.puzzle.update()
            elif event.key == K_s or event.key == K_DOWN: game.direction = pygame.Vector2(0,1)
            elif event.key == K_a or event.key == K_LEFT: game.direction = pygame.Vector2(-1,0)
            elif event.key == K_d or event.key == K_RIGHT: game.direction = pygame.Vector2(1,0)

    pygame.display.update()

pygame.quit()