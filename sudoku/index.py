from sudoku import *
import sys





# ------------------------------ Tests Initials



# S = Sudoku()
# print("Initial :")
# S.display()
# S.display_numof_possibilities()

# S.set_tile(0, 0, 1)
# S.set_tile(0, 1, 0)
# S.update_possibilities()

# # print(S.check_lines())
# # print(S.check_cols())
# # print(S.check_boxes())


# print("Updated :")
# S.display()
# S.display_numof_possibilities()

# --------------------------- Exemple 1 ---------------------------------------

# N = None
# S1 = Sudoku()

# S1.grid = [
#         [N, N, N,   N, N, N,   0, N, N],
#         [N, N, N,   N, N, N,   N, N, N],
#         [N, N, N,   N, N, N,   N, N, N],

#         [N, N, N,   N, N, N,   N, N, N],
#         [N, N, N,   N, N, N,   N, 0, N],
#         [N, N, N,   N, N, N,   N, N, N],

#         [0, N, N,   N, N, N,   1, 2, 3],
#         [N, N, N,   0, N, N,   4, 5, 6],
#         [N, N, N,   N, N, N,   7, 8, N]
# ]
        
# S1.update_possibilities()

# gap()

# S1.display()
# S1.display_numof_possibilities()

# gap()

# wfc_stop(S1)


# S1.display()
# S1.display_numof_possibilities()

# ------------------------- Exemple 2 -------------------------------------

# gap()
# S2 = Sudoku()
# N = None
# S2.grid = [
#         [N, 1, N,   N, N, N,   6, N, 0],
#         [0, 4, N,   N, N, 2,   1, N, N],
#         [N, N, 5,   4, N, N,   N, 8, N],

#         [1, N, 4,   2, 3, N,   8, N, N],
#         [3, N, 0,   8, N, N,   N, 2, N],
#         [N, N, N,   N, 6, 0,   5, N, 4],

#         [N, N, N,   0, N, N,   3, N, N],
#         [4, 3, N,   N, N, 6,   N, N, 7],
#         [7, N, 6,   N, N, N,   N, 5, 2]
# ]

# S2.update_possibilities()

# S2.display()
# S2.display_numof_possibilities()

# gap()

# wfc_stop(S2)


# S2.display()
# S2.display_numof_possibilities()

# --------- Exemple 3 ----------

# gap()
# S3 = Sudoku()
# N = None
# S3.grid = [
#         [N, 1, N,   N, N, N,   6, N, 0],
#         [0, 4, N,   N, N, 2,   1, N, N],
#         [N, N, 5,   4, N, N,   N, 8, N],

#         [1, N, 4,   N, 3, N,   8, N, N],
#         [3, N, 0,   8, N, N,   N, 2, N],
#         [N, N, N,   N, 6, 0,   N, N, 4],

#         [N, N, N,   0, N, N,   3, N, N],
#         [4, 3, N,   N, N, 6,   N, N, 7],
#         [7, N, 6,   N, N, N,   N, 5, 2]
# ]

# S3.update_possibilities()

# S3.display()
# S3.display_numof_possibilities()

# gap()

# wfc_stop(S3)


# S3.display()
# S3.display_numof_possibilities()

# --------------- Exemple 4 -----------

# N = None
# S1 = Sudoku()

# S1.grid = [
#         [N, N, N,   N, N, N,   0, N, N],
#         [N, N, N,   N, N, N,   N, N, N],
#         [N, N, N,   N, N, N,   N, N, N],

#         [N, N, N,   N, N, N,   N, N, N],
#         [N, N, N,   N, N, N,   N, 0, N],
#         [N, N, N,   N, N, N,   N, N, N],

#         [0, N, N,   N, N, N,   N, N, N],
#         [N, N, N,   0, N, N,   N, N, N],
#         [N, N, N,   N, N, N,   N, N, N]
# ]
        
# S1.update_possibilities()

# gap()

# S1.display()
# S1.display_numof_possibilities()

# gap()

# wfc_stop(S1)


# S1.display()
# S1.display_numof_possibilities()


# ------  GRILLE DE BASE -------------
# N = None
# S.grid = [
#         [N, N, N,   N, N, N,   N, N, N],
#         [N, N, N,   N, N, N,   N, N, N],
#         [N, N, N,   N, N, N,   N, N, N],

#         [N, N, N,   N, N, N,   N, N, N],
#         [N, N, N,   N, N, N,   N, N, N],
#         [N, N, N,   N, N, N,   N, N, N],

#         [N, N, N,   N, N, N,   N, N, N],
#         [N, N, N,   N, N, N,   N, N, N],
#         [N, N, N,   N, N, N,   N, N, N]
# ]


# ------------ Algorithme 2: random collapse -----------------

# ---------- Exemple 1: ex dysfonctionel avec algo précédent -


# S3 = Sudoku()
# N = None
# gap()

# S3.grid = [
#         [N, 1, N,   N, N, N,   6, N, 0],
#         [0, 4, N,   N, N, 2,   1, N, N],
#         [N, N, 5,   4, N, N,   N, 8, N],

#         [1, N, 4,   N, 3, N,   8, N, N],
#         [3, N, 0,   8, N, N,   N, 2, N],
#         [N, N, N,   N, 6, 0,   N, N, 4],

#         [N, N, N,   0, N, N,   3, N, N],
#         [4, 3, N,   N, N, 6,   N, N, 7],
#         [7, N, 6,   N, N, N,   N, 5, 2]
# ]

# wfc_rand(S3)


# ----------- Exemple 2 ------------

# N = None
# S1 = Sudoku()
# gap()

# S1.grid = [
#         [N, N, N,   N, N, N,   0, N, N],
#         [N, N, N,   N, N, N,   N, N, N],
#         [N, N, N,   N, N, N,   N, N, N],

#         [N, N, N,   N, N, N,   N, N, N],
#         [N, N, N,   N, N, N,   N, 0, N],
#         [N, N, N,   N, N, N,   N, N, N],

#         [0, N, N,   N, N, N,   N, N, N],
#         [N, N, N,   0, N, N,   N, N, N],
#         [N, N, N,   N, N, N,   N, N, N]
# ]
        
# wfc_rand(S1)

# ------------------- Ex 3 -------------

N = None
S = Sudoku()
gap()

S.grid = [
        [N, N, N,   N, N, N,   N, N, N],
        [N, N, N,   N, N, N,   N, N, N],
        [N, N, N,   N, N, N,   N, N, N],

        [N, N, N,   N, N, N,   N, N, N],
        [N, N, N,   N, N, N,   N, N, N],
        [N, N, N,   N, N, N,   N, N, N],

        [N, N, N,   N, N, N,   N, N, N],
        [N, N, N,   N, N, N,   N, N, N],
        [N, N, N,   N, N, N,   N, N, N]
]

wfc_rand(S)
