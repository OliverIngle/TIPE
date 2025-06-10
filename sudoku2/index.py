import numpy as np
import sys
from sudoku import *
import time



# ---- None marker ---
N = None
# ---- ----------- ----

# --------------------- Test 0 ----------------------

# S1 = Sudoku(2)
# # print(S1.grid)
# # print(S1.entropies)

# # S1.force_infere([
# #     [0, 1, N, 1],
# #     [1, N, N, N],
# #     [N, N, N, N],
# #     [1, N, N, N]
# # ])

# S1.infere_and_reduce([
#     [0, 3, N, 1],
#     [1, N, N, N],
#     [N, N, N, N],
#     [N, N, N, N]
# ])
# wfc(S1)
# S1.view()


# -------------------------------------------
# success = 0
# n = 100000
# for i in range(n):
#     sys.stdout.write("\x1b[1A\x1b[2K")
#     S1 = Sudoku(3)
#     if wfc(S1):
#         success += 1
#     p = np.format_float_positional(i/n * 100, precision=1)
#     print(f"\033[94m{p}%\033[0m")

# pourcent = success / n * 100
# print(f"Le sudoku est resolu \033[92m{pourcent}%\033[0m du temps")
# -------
# S = Sudoku(2)
# t1 = time.time()
# success = wfc_min_entropy(S)
# t2 = time.time()
# print(t2 - t1)
# print(success)
# S.view()
# print(S.number_of_completed())


# ------------ Test 1 - Grilles n x n vides, comparaion max/min entropy ------------

# n = 1000
# dimension = 4
# max_entropie_successes = 0
# min_entropie_successes = 0

# max_entropie_completion = 0
# min_entropie_completion = 0

# print("\n\n")
# print("Test: comparaison heuristique choix entropie min/max avec une grille vide")
# print("Parametres:")
# print(f"Grilles:            {dimension**2} x {dimension**2}")
# print(f"Nombre d'essais:    {n}")
# print("\n")

# print("Version choix de l'entropie minimale\n")
# for i in range(n):
#     S = Sudoku(dimension)
#     success = wfc_min_entropy(S)
#     if success:
#         min_entropie_successes += 1
#     min_entropie_completion += S.number_of_completed()
#     sys.stdout.write("\x1b[1A\x1b[2K")
#     p = np.format_float_positional(i/n * 100, precision=1)
#     print(f"Progrés:            \033[94m{p}%\033[0m")

# print("\n")

# min_entropie_successes_pourcent = min_entropie_successes / n * 100
# min_entropie_competion_avg = min_entropie_completion / n

# print(f"Le sudoku est resolu \033[92m{min_entropie_successes_pourcent}%\033[0m du temps ({min_entropie_successes}).")
# print(f"En moyene, wfc resolve \033[93m{min_entropie_competion_avg}/{dimension**4}\033[0m cases.")

# print("\n")
# print("Version choix de l'entropie maximale\n")

# for i in range(n):
#     S = Sudoku(dimension)
#     success = wfc_max_entropy(S)
#     if success:
#         max_entropie_successes += 1
#     max_entropie_completion += S.number_of_completed()
#     sys.stdout.write("\x1b[1A\x1b[2K")
#     p = np.format_float_positional(i/n * 100, precision=1)
#     print(f"Progrés:            \033[94m{p}%\033[0m")

# max_entropie_successes_pourcent = max_entropie_successes / n * 100
# max_entropie_competion_avg = max_entropie_completion / n

# print("\n")
# print(f"Le sudoku est resolu \033[92m{max_entropie_successes_pourcent}%\033[0m du temps ({max_entropie_successes}).")
# print(f"En moyene, wfc resolve \033[93m{max_entropie_competion_avg}/{dimension**4}\033[0m cases.")

# ------------ Test 2 - idem avec grille commencé.

# n = 10000
# dimension = 3
# max_entropie_successes = 0
# min_entropie_successes = 0

# max_entropie_completion = 0
# min_entropie_completion = 0

# grille = [
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

# print("\n\n")
# print("Test: comparaison heuristique choix entropie min/max avec une grille vide")
# print("Parametres:")
# print(f"Grilles:            {dimension**2} x {dimension**2}")
# print(f"Nombre d'essais:    {n}")
# print("\n")

# print("Version choix de l'entropie minimale\n")
# for i in range(n):
#     S = Sudoku(dimension)
#     S.infere_and_reduce(grille)
#     success = wfc_min_entropy(S)
#     if success:
#         min_entropie_successes += 1
#     min_entropie_completion += S.number_of_completed()
#     sys.stdout.write("\x1b[1A\x1b[2K")
#     p = np.format_float_positional(i/n * 100, precision=1)
#     print(f"Progrés:            \033[94m{p}%\033[0m")

# print("\n")

# min_entropie_successes_pourcent = min_entropie_successes / n * 100
# min_entropie_competion_avg = min_entropie_completion / n

# print(f"Le sudoku est resolu \033[92m{min_entropie_successes_pourcent}%\033[0m du temps ({min_entropie_successes}).")
# print(f"En moyene, wfc resolve \033[93m{min_entropie_competion_avg}/{dimension**4}\033[0m cases.")

# print("\n")
# print("Version choix de l'entropie maximale\n")

# for i in range(n):
#     S = Sudoku(dimension)
#     S.infere_and_reduce(grille)
#     success = wfc_max_entropy(S)
#     if success:
#         max_entropie_successes += 1
#     max_entropie_completion += S.number_of_completed()
#     sys.stdout.write("\x1b[1A\x1b[2K")
#     p = np.format_float_positional(i/n * 100, precision=1)
#     print(f"Progrés:            \033[94m{p}%\033[0m")

# max_entropie_successes_pourcent = max_entropie_successes / n * 100
# max_entropie_competion_avg = max_entropie_completion / n

# print("\n")
# print(f"Le sudoku est resolu \033[92m{max_entropie_successes_pourcent}%\033[0m du temps ({max_entropie_successes}).")
# print(f"En moyene, wfc resolve \033[93m{max_entropie_competion_avg}/{dimension**4}\033[0m cases.")

# ------ Sous test ------

grille = [
        [N, N, N,   N, N, N,   0, N, N],
        [N, N, N,   N, N, N,   N, N, N],
        [N, N, N,   N, N, N,   N, N, N],

        [N, N, N,   N, N, N,   N, N, N],
        [N, N, N,   N, N, N,   N, 0, N],
        [N, N, N,   N, N, N,   N, N, N],

        [0, N, N,   N, N, N,   N, N, N],
        [N, N, N,   0, N, N,   N, N, N],
        [N, N, N,   N, N, N,   N, N, N]
]

for _ in range(100):
    S = Sudoku(3)
    S.infere_and_reduce(grille)
    wfc_max_entropy(S)
    input()
