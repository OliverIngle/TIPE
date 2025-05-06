
import random
from PIL.Image import new
from numpy import positive

gap_txt = ""
for i in range(100):
    gap_txt += "\n"

def gap():
    _ = input()
    print(gap_txt)

class Sudoku:
    grid =[[None for _ in range(9)] for _ in range(9)]
    possibilities = [[[i for i in range(9)] for _ in range(9)] for _ in range(9)]

    def display(self):
        s = ""
        for l in self.grid:
            for elm in l:
                if elm == None:
                    s += ". "
                else:
                    s += f"{elm} "
            s += "\n"
        print(s)

    def display_numof_possibilities(self):
        s = ""
        for l in self.possibilities:
            for elm in l:
                x = len(elm)
                s += f"{x} "
            s += "\n"
        print(s)


    def set_tile(self, x, y, val):
        self.grid[x][y] = val

    def check_line(self, n):
        line = self.grid[n]
        for i in range(len(line)):
            el = line[i]
            for j in range(i + 1, len(line)):
                if line[j] == None:
                    continue
                if line[j] == el:
                    return False
        return True

    def check_lines(self):
        for i in range(9):
            if not self.check_line(i):
                return False
        return True

    def check_col(self, n):
        g = self.grid
        for i in range(9):
            el = g[i][n]
            for j in range(i + 1, 9):
                if g[j][n] == None:
                    continue
                if g[j][n] == el:
                    return False
        return True

    def check_cols(self):
        for i in range(9):
            if not self.check_col(i):
                return False
        return True

        

    def getbox(self, x, y):
        g = self.grid
        L = [g[i+(3*x)][(y*3):(y*3)+3] for i in range(3)]
        return L

    def getbox_L(self, x , y):
        g = self.grid
        L = []
        for i in range(3):
            L += g[i+(3*x)][(y*3):(y*3)+3]
        return L 
    
    def boxes_L(self):
        L = []
        for i in range(3):
            for j in range(3):
                L.append(self.getbox_L(i, j))
        return L


    def check_boxes(self):
        for box in self.boxes_L():
            for i in range(len(box)):
                el = box[i]
                for j in range(i + 1, len(box)):
                    if box[j] == None:
                        continue
                    if box[j] == el:
                        return False
        return True

    def check(self):
        return self.check_lines() and self.check_cols() and self.check_boxes()

    def update_possibilities(self):
        g = self.grid
        p = self.possibilities
        for i in range(9):
            for j in range(9):
                if g[i][j] != None:
                    p[i][j] = []
                    continue
                nums = p[i][j]
                new_nums = []
                for n in nums:
                    self.set_tile(i, j, n)
                    cond = self.check()
                    if cond:
                        new_nums.append(n)
                g[i][j] = None
                p[i][j] = new_nums


                
def wfc_stop(S: Sudoku):
    if S.check() == False:
        print("Invalid Sudoku")
        return
    flag = True
    while flag:
        flag = False
        for i in range(9):
            for j in range(9):
                if S.grid[i][j] != None:
                    continue
                p = S.possibilities[i][j]
                if len(p) == 1:
                    S.set_tile(i, j, p[0])
                    flag = True
        S.update_possibilities()
        S.display()                         #---------
        S.display_numof_possibilities()     #---------
        gap()
            
def wfc_rand(S: Sudoku):
    if S.check() == False:
        print("Invalid Sudoku")
        return
    flag = True
    while flag:

        S.update_possibilities()
        S.display()                         #---------
        S.display_numof_possibilities()     #---------
        gap()
            
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

N = None
S1 = Sudoku()

S1.grid = [
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
        
S1.update_possibilities()

gap()

S1.display()
S1.display_numof_possibilities()

gap()

wfc_stop(S1)


S1.display()
S1.display_numof_possibilities()


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
