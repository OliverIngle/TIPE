
import random
from PIL.Image import new
from numpy import positive
import sys

gap_txt = ""
for i in range(100):
    gap_txt += "\n"

def gap():
    _ = input()
    print(gap_txt)


def printstd(txt):
    sys.stdout.write(txt)

def wipelines(n):
    for _ in range(n):
        sys.stdout.write("\x1b[1A\x1b[2K")


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

    def serealize(self):
        s = ""
        for l in self.grid:
            for elm in l:
                if elm == None:
                    s += ". "
                else:
                    s += f"{elm} "
            s += "\n"
        s += "\n"
        for l in self.possibilities:
            for elm in l:
                x = len(elm)
                s += f"{x} "
            s += "\n"
        return s





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
    S.update_possibilities()
    while True:
        min_entropy = 9
        x, y = None, None
        for i in range(9):
            for j in range(9):
                l = len(S.possibilities[i][j])
                if l == 0:
                    continue
                elif l <= min_entropy:
                    min_entropy = l
                    x = i
                    y = j
        if x == None or y == None:
            return
        elif min_entropy == 1:
            S.set_tile(x, y, S.possibilities[x][y][0])
        else:
            i = random.randint(1, min_entropy) - 1
            S.set_tile(x, y, S.possibilities[x][y][i])

        S.update_possibilities()
        # wipelines(20)
        # printstd(S.serealize())
            


