import numpy as np
import sys

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
    while tag:
        tag = False
        min_entropy = s
        min_entropy_coords = []
        for i in range(s):
            for j in range(s):
                entropies = S.entropies[i][j]
                n_entropies = len(entropies)
                if n_entropies == 0:
                    continue
                if n_entropies == 1:
                    S.place_and_reduce(i, j, entropies[0])
                    tag = True


# ---- None marker ----
N = None
# ---- ----------- ----


S1 = Sudoku(2)
# print(S1.grid)
# print(S1.entropies)

# S1.force_infere([
#     [0, 1, N, 1],
#     [1, N, N, N],
#     [N, N, N, N],
#     [1, N, N, N]
# ])

S1.view()
S1.infere_and_reduce([
    [0, 3, N, 1],
    [1, N, N, N],
    [N, N, N, N],
    [N, N, N, N]
])
input()
S1.update_view()
input()
wfc(S1)

S1.update_view()
