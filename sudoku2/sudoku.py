import numpy as np
import sys
import random

def reduce(L, x):
    N = []
    for el in L:
        if el == x:
            continue
        N.append(el)
    return N

class Sudoku:
    def __init__(self, n):
        self.n = n
        self.s = n * n
        self.grid = [ [None for _ in range(self.s)] for _ in range(self.s) ]
        self.entropies = [ [[i for i in range(self.s)] for _ in range(self.s)] for _ in range(self.s)]

    def serealize(self):
        s = ""
        for col in self.grid:
            for x in col:
                if x == None:
                    s += ". "
                    continue
                s += f"{x} "
            s += "\n"
        s += "\n"
        for col in self.entropies:
            for l in col:
                x = len(l)
                if x == 0:
                    s += "- "
                    continue
                s += f"{x} "
            s += "\n"
        return s

    def view(self):
        s = self.serealize()
        sys.stdout.write(s)

    def update_view(self):
        for _ in range(self.s * 2 + 2):
            sys.stdout.write("\x1b[1A\x1b[2K")
        self.view()

    def checkrow(self, i):
        row = self.grid[i]
        for j in range(self.s):
            x = row[j]
            if x == None:
                continue
            for k in range(j + 1, self.s):
                if row[k] == x:
                    return False
        return True

    def checkcol(self, j):
        for i in range(self.s):
            x = self.grid[i][j]
            if x == None:
                continue
            for k in range(i + 1, self.s):
                if self.grid[k][j] == x:
                    return False
        return True

    def box_coords(self, i, j):
        x = int((np.floor(i/self.n) * self.n))
        y = int((np.floor(j/self.n) * self.n))
        coords = []
        for k in range(self.n):
            for l in range(self.n):
                coords.append((x + k, y + l))
        return coords

    def checkbox(self, i, j):
        coords = self.box_coords(i, j)
        for k in range(self.s):
            (x, y) = coords[k]
            a = self.grid[x][y]
            if a == None:
                continue
            for l in range(k + 1, self.s):
                (b, c) = coords[l]
                if self.grid[b][c] == a:
                    return False
        return True
                


    def force_place(self, i, j, n):
        self.grid[i][j] = n

    def place_and_reduce(self, i, j, n):
        self.grid[i][j] = n
        coords = self.box_coords(i, j)
        for k in range(self.s):
            self.entropies[i][k] = reduce(self.entropies[i][k], n)
            self.entropies[k][j] = reduce(self.entropies[k][j], n)
            (x, y) = coords[k]
            self.entropies[x][y] = reduce(self.entropies[x][y], n)
        self.entropies[i][j] = []

    
    def force_infere(self, L):
        for i in range(self.s):
            for j in range(self.s):
                self.grid[i][j] = L[i][j]
    # HANDLE FOR None !!!!!!!!!!!!!!!!!!
    def infere_and_reduce(self, L):
        for i in range(self.s):
            for j in range(self.s):
                x = L[i][j]
                if x == None:
                    continue
                self.place_and_reduce(i, j, x)

def wfc(S):
    s = S.s
    tag = True
    contraditcion = False
    while tag:
        tag = False
        min_entropy = s
        min_entropy_coords = []
        for i in range(s):
            for j in range(s):
                entropies = S.entropies[i][j]
                n_entropies = len(entropies)
                if n_entropies == 0:
                    if S.grid[i][j] == None:
                        S.force_place(i, j, "\033[31;1mC\033[0m")
                        contraditcion = True
                    continue
                elif n_entropies == 1:
                    S.place_and_reduce(i, j, entropies[0])
                    tag = True
                    break
                elif n_entropies == min_entropy:
                    min_entropy_coords.append((i, j))
                elif n_entropies < min_entropy:
                    min_entropy = n_entropies
                    min_entropy_coords = [(i, j)]
            if tag or contraditcion:
                break
        if tag or min_entropy_coords == [] or contraditcion:
            # S.update_view()
            continue
        r = random.randint(0, len(min_entropy_coords) - 1)
        (x, y) = min_entropy_coords[r]
        r2 = random.randint(0, min_entropy - 1)
        el = S.entropies[x][y][r2]
        S.place_and_reduce(x, y, el)
        tag = True
        # input()
        # S.update_view()

    return not contraditcion





# ---- None marker ----
N = None
# ---- ----------- ----

# --------------------- Test 1 ----------------------

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


# --------------------- Test 2 ----------------------
success = 0
n = 100000
for i in range(n):
    sys.stdout.write("\x1b[1A\x1b[2K")
    S1 = Sudoku(3)
    if wfc(S1):
        success += 1
    print(f"\033[94m{np.round(i/n * 100)}%\033[0m")

pourcent = success / n * 100
print(f"Le sudoku est resolu \033[92m{pourcent}%\033[0m du temps")
