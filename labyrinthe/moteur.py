import sys
import time
import random
import numpy as np

W = "W"
U = "U"
H = "H"

def rmLines(n):
    for _ in range(n):
        sys.stdout.write("\x1b[1A\x1b[2K")

class Labyrinthe:
    def __init__(self, n):
        self.n = n
        self.grid = [
                [ "U" for _ in range(n) ] for _ in range(n)
                ]
        self.grid[0][0] = "S"
        self.grid[n-1][n-1] = "F"

    def serealize(self):
        s = ""
        for i in range(self.n):
            for j in range(self.n):
                tile_type = self.grid[i][j]
                if tile_type == "W":
                    s += "  "
                elif tile_type == "H":
                    s += "\033[0;107m  \033[0m"
                elif tile_type == "U":
                    s += "\033[47m  \033[0m"
                elif tile_type == "S" or tile_type == "F":
                    s += "\033[41m  \033[0m"
                elif tile_type == "X":
                    s += "\033[45m  \033[0m"
                elif tile_type == "C":
                    s += "\033[44m  \033[0m"
                else:
                    s += "  "
            if i == self.n - 1:
                break
            s += "\n"
        s += "\n"
        return s

    def display(self):
        sys.stdout.write(self.serealize())

    def updateDisplay(self): 
        for _ in range(self.n):
            sys.stdout.write("\x1b[1A\x1b[2K")
        sys.stdout.write(self.serealize())

    def displayCoord(self, x, y):
        rmLines(self.n)
        tileType = self.grid[x][y]
        self.grid[x][y] = "X"
        sys.stdout.write(self.serealize())
        self.grid[x][y] = tileType

    def displayCollapsableAndCoord(self, x, y, L):
        rmLines(self.n)
        tiles = []
        for k in range(len(L)):
            i, j = L[k]
            tiles.append(self.grid[i][j])
            self.grid[i][j] = "C"
        tileType = self.grid[x][y]
        self.grid[x][y] = "X"
        sys.stdout.write(self.serealize())
        self.grid[x][y] = tileType 
        for k in range(len(L)):
            i, j = L[k]
            self.grid[i][j] = tiles[k]

    def displayCollapsable(self, L):
        rmLines(self.n)
        tiles = []
        for k in range(len(L)):
            i, j = L[k]
            tiles.append(self.grid[i][j])
            self.grid[i][j] = "C"
        sys.stdout.write(self.serealize())
        for k in range(len(L)):
            i, j = L[k]
            self.grid[i][j] = tiles[k]

    def placeWall(self, x, y):
        self.grid[x][y] = "W"
    
    def placeHall(self, x, y):
        self.grid[x][y] = "H"

    def adjacent(self, x, y):
        g = self.grid
        n = self.n
        if n == 1:
            return [g[0][0]]
        if x == 0 and y == 0:
            adj = [
                    ["W",     "W",     "W"],
                    ["W", g[0][0], g[0][1]],
                    ["W", g[1][0], g[1][1]]
                ]
            return adj
        elif x == 0 and y == n - 1:
            adj = [
                    ["W",       "W",       "W"],
                    [g[0][n-2], g[0][n-1], "W"],
                    [g[1][n-2], g[1][n-1], "W"]
                ]
            return adj
        elif x == 0:
            adj = [
                    ["W",       "W",       "W"],
                    [g[0][y-1], g[0][y], g[0][y+1]],
                    [g[1][y-1], g[1][y], g[1][y+1]]
                ]
            return adj
        elif x == n-1 and y == 0:
            adj = [
                    ["W", g[n-2][0], g[n-2][1]],
                    ["W", g[n-1][0], g[n-1][0]],
                    ["W",       "W",       "W"]
                ]
            return adj
        elif x == n-1 and y == n-1:
            adj = [
                    [g[n-2][n-2], g[n-2][n-2], "W"],
                    [g[n-1][n-2], g[n-1][n-1], "W"],
                    [        "W",       "W",   "W"]
                ]
            return adj
        elif x == n-1:
            adj = [
                    [g[n-2][y-1], g[n-2][y], g[n-2][y+1]],
                    [g[n-1][y-1], g[n-1][y], g[n-1][y+1]],
                    [        "W",       "W",         "W"]
                ]
            return adj
        elif y == 0:
                adj = [
                    ["W", g[x-1][y], g[x-1][y+1]],
                    ["W",   g[x][y],   g[x][y+1]],
                    ["W", g[x+1][y], g[x-1][y+1]]
                ]
                return adj

        elif y == n-1:
            adj = [
                    [g[x-1][y-1], g[x-1][y], "W"],
                    [g[x][y-1],   g[x][y],   "W"],
                    [g[x+1][y-1], g[x+1][y], "W"]
                ]
            return adj

        else:
            adj = [
                    [g[x-1][y-1], g[x-1][y], g[x-1][y+1]],
                    [g[x][y-1],   g[x][y],   g[x][y+1]  ],
                    [g[x+1][y-1], g[x+1][y], g[x+1][y+1]]
                ]
            return adj








def serealizeBlock(b):
    n = len(b)
    s = ""
    for i in range(n):
        for j in range(n):
            tile_type = b[i][j]
            if tile_type == "W":
                s += "  "
            elif tile_type == "H":
                s += "\033[107m  \033[0m"
            elif tile_type == "U":
                s += "\033[47m  \033[0m"
            elif tile_type == "S" or tile_type == "F":
                s += "\033[41m  \033[0m"
            else:
                s += "  "
        if i == n - 1:
            break
        s += "\n"
    s += "\n"
    return s

def debug(l: Labyrinthe, adj, i, j, collapsable, comment, pause):
    l.displayCollapsableAndCoord(i, j, collapsable)
    print(f"Analyzing {i}, {j} -> {comment}")
    print(serealizeBlock(adj))
    if pause:
        input()
        rmLines(6)
    else:
        # time.sleep(0.005)
        rmLines(5)


def distBetweenPoints(x1, y1, x2, y2):
    dx = np.sqrt((x2 - x1)**2)
    dy = np.sqrt((y2 - y1)**2)
    dist = np.sqrt(dx**2 + dy**2)
    return dist


def favorCenterSelec(L, n, f):
    R = []
    cx = n / 2
    cy = cx
    centerToCorners = distBetweenPoints(0, 0, cx, cy)
    for i in range(len(L)):
        x, y = L[i]
        d = distBetweenPoints(x, y, cx, cy)
        relativeFromConrner = centerToCorners - d
        nb_adds = int(np.floor(f(relativeFromConrner)) + 1)
        for _ in range(nb_adds):
            R.append((x, y))
    return random.choice(R)
    


def wfc(l: Labyrinthe):
    complete = False
    n = l.n
    while not complete:
        complete = True
        collapsable = []
        auto_collapsed = False
        for i in range(n):
            for j in range(n):


                if l.grid[i][j] != "U":
                    # debug(l, l.adjacent(i, j), i, j, collapsable, "Tile already placed.", False)
                    continue
                complete = False
                adj = l.adjacent(i, j)


                
                match adj:
                    # Edges with nothing in vicinity
                    case [  # Top edge, nothing in vivinity
                            ["W",       "W",         "W"      ],
                            ["U" | "H", "U",         "U" | "H"],
                            ["U" | "H", "U" | "H",   "U" | "H"]
                        ]:
                        # debug(l, adj, i, j, collapsable, "Adding to collapsable.", False)
                        collapsable.append((i, j)) 

                    case [  # Top edge, auto collapsable to Hall
                            ["W",       "W",         "W"      ],
                            ["W",       "U",         "U" | "H"],
                            ["U" | "H", "U" | "H",   "U" | "H"]
                        ] | [
                            ["W",       "W",         "W"      ],
                            ["U" | "H", "U",         "W"      ],
                            ["U" | "H", "U" | "H",   "U" | "H"]
                        ]:
                            l.placeHall(i, j)
                            # debug(l, adj, i, j, collapsable, "Auto collapsing to Hall", False)
                            auto_collapsed = True

                    case [  # Left edge, nothing in vicinity
                            ["W", "U" | "H",     "U" | "H"],
                            ["W", "U",           "U" | "H"],
                            ["W", "U" | "H",     "U" | "H"]
                        ]:
                        # debug(l, adj, i, j, collapsable, "Adding to collapsable", False)
                        collapsable.append((i, j))
                    case [  # Left edge, auto collapse to hall
                            ["W", "W",           "U" | "H"],
                            ["W", "U",           "U" | "H"],
                            ["W", "U" | "H",     "U" | "H"]
                        ] | [
                            ["W", "U" | "H",     "U" | "H"],
                            ["W", "U",           "U" | "H"],
                            ["W", "W",           "U" | "H"]
                        ]:
                            l.placeHall(i, j)
                            # debug(l, adj, i, j, collapsable, "Auto collapsing to Hall", False)
                            auto_collapsed = True

                    case [  # Right edge, nothing in vicinity
                            ["U" | "H",    "U" | "H", "W"],
                            ["U" | "H",    "U"      , "W"],
                            ["U" | "H",    "U" | "H", "W"]
                        ]:
                        collapsable.append((i, j))
                    case [  # Right edge, auto collapse
                            ["U" | "H",    "W"      , "W"],
                            ["U" | "H",    "U"      , "W"],
                            ["U" | "H",    "U" | "H", "W"]
                        ] | [
                            ["U" | "H",    "U" | "H", "W"],
                            ["U" | "H",    "U"      , "W"],
                            ["U" | "H",    "W"      , "W"]
                        ]:
                            l.placeHall(i, j)
                            # debug(l, adj, i, j, collapsable, "Auto collapsing to Hall", False)
                            auto_collapsed = True

                    case [  # Bottom edge, nothing in vicinity
                            ["U" | "H", "U" | "H", "U" | "H"],
                            ["U" | "H", "U"      , "U" | "H"],
                            ["W"      , "W"      , "W"      ]
                          ]:
                        collapsable.append((i, j))
                    case [  # Bottom edge, auto collapse
                            ["U" | "H", "U" | "H", "U" | "H"],
                            ["W"      , "U"      , "U" | "H"],
                            ["W"      , "W"      , "W"      ]
                          ] | [  
                            ["U" | "H", "U" | "H", "U" | "H"],
                            ["U" | "H", "U"      , "W"      ],
                            ["W"      , "W"      , "W"      ]
                         ]:
                            l.placeHall(i, j)
                            # debug(l, adj, i, j, collapsable, "Auto collapsing to Hall", False)
                            auto_collapsed = True
                    
                    # ADD to COLLAPSABLE
                    case [
                            [_        , "W"      , _        ],
                            ["U" | "H", _        , "U" | "H"],
                            ["U" | "H", "U" | "H", "U" | "H"]
                          ] | [
                            [_  , "U" | "H", "U" | "H"],
                            ["W", _        , "U" | "H"],
                            [_  , "U" | "H", "U" | "H"]
                          ] | [
                            ["U" | "H", "U" | "H", _  ],
                            ["U" | "H", _        , "W"],
                            ["U" | "H", "U" | "H", _  ]
                          ] | [
                            ["U" | "H", "U" | "H", "U" | "H"],
                            ["U" | "H", _        , "U" | "H"],
                            [_        , "W"      , _        ]
                        ]:
                            collapsable.append((i, j))
                    # COLLPASES to HALL
                    case [
                            _            ,
                            ["W", _, "W"],
                            _

                          ] | [

                            [_, "W", _],
                            _          ,
                            [_, "W", _]

                          ] | [

                            [_  , "W", _],
                            ["W", _  , _],
                            _

                          ] | [

                            [_, "W",   _],
                            [_, _  , "W"],
                            _

                          ] | [

                            _            ,
                            ["W", _  , _],
                            [_, "W",   _],

                          ] | [

                            _            ,
                            [_, _  , "W"],
                            [_, "W",   _]

                        ]:
                            l.placeHall(i, j)
                            # debug(l, adj, i, j, collapsable, "Auto collapsing to Hall", False)
                            auto_collapsed = True


                    case _:                
                        # debug(l, adj, i, j, collapsable, "No case yet", False)
                        continue

        if not auto_collapsed and collapsable != []:
            l.displayCollapsable(collapsable)
            time.sleep(0.001)
            # x, y = favorCenterSelec(collapsable, n, lambda x: x)
            x, y = random.choice(collapsable)
            l.placeWall(x, y)
        if not auto_collapsed and collapsable == []:
            complete = True
            l.updateDisplay()
    for i in range(n):
        for j in range(n):
            if l.grid[i][j] == "U":
                l.placeHall(i, j)
    l.updateDisplay()
                
    

# n = int(input())
n = 15
while True:
    l1 = Labyrinthe(n)
    l1.display()

    wfc(l1)
    l1.updateDisplay()
    # input()
