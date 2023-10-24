from .puzzle import I, J, L, O, S, T, Z


puzzle_t = T()
puzzle_o = O()
puzzle_s = S()
puzzle_z = Z()
puzzle_i = I()
puzzle_l = L()
puzzle_j = J()
puzzles = [puzzle_t, puzzle_i, puzzle_j, puzzle_l, puzzle_o, puzzle_z, puzzle_s]


__all__ = [
    "puzzle_t",
    "puzzle_o",
    "puzzle_s",
    "puzzle_z",
    "puzzle_i",
    "puzzle_l",
    "puzzle_j",
    "puzzles",
]
