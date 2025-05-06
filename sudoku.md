# WaveFunctionCollapse pour résoudre un sudoku

Une premiètre utilisation de l'algorithme wfc est de réoudre des sudokus

## La classe sudoku

### Bases

```python
class Sudoku:
    grid:           list
    possibilities:  list
```
Ici `grid` est une liste 2-dimensionelle pour stocker les nombres placés dans notre sudoku.
```python
grid =[[None for _ in range(9)] for _ in range(9)]
```

`possibilities` est une liste 3 dimensionelle ou on pourra stocker les choix possibles pour une case vide

```python
possibilities = [[[i for i in range(9)] for _ in range(9)] for _ in range(9)]
```

### Validité du sudoku

Plusieur fonctions pour vérifier la validité du sudoku selon les règles ordinires du jeux

- Lignes
```python
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
```

- Colonnes
```python
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
```

- Cases 3x3
```python
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
```

### Génération des possibilités pour les cases vides

Cette fonction parcours les cases vides en essayand d'y placer les différent chiffres.

Si le placement d'un chiffre n'invalide pas le sudoku, il est rajouté dans la liste de chiffres possibles pour la case en question.

```python
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
```

## Un premier algorithme WFC

1) Génerer la liste de posibilités pour chaque case vide. Pluse une case a de posibilités, plus elle a d' "entropie".
2) Parcourir les cases vides
    - Si une case n'a qu'une seule posibilité, completer cette case.
3) Si aucune case n'a été modifié, s'arreter. Sinon, repasser a l'étape **1**.

```python
def wfc_stop(S: Sudoku):
    if S.check() == False:
        print("Invalid Sudoku")
        return
    flag = True
    while flag:
        flag = False
        S.update_possibilities()
        for i in range(9):
            for j in range(9):
                if S.grid[i][j] != None:
                    continue
                p = S.possibilities[i][j]
                if len(p) == 1:
                    S.set_tile(i, j, p[0])
                    print("colapsing", i, j)
                    flag = True

    print("Stopped")
```
### Test 1

```
. . . . . . 0 . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . 0 .
. . . . . . . . .
0 . . . . . 1 2 3
. . . 0 . . 4 5 6
. . . . . . 7 8 .
```

### Test 2

```
. 1 . . . . 6 . 0
0 4 . . . 2 1 . .
. . 5 4 . . . 8 .
1 . 4 2 3 . 8 . .
3 . 0 8 . . . 2 .
. . . . 6 0 5 . 4
. . . 0 . . 3 . .
4 3 . . . 6 . . 7
7 . 6 . . . . 5 2
```

### Test 3

```
. 1 . . . . 6 . 0
0 4 . . . 2 1 . .
. . 5 4 . . . 8 .
1 . 4 . 3 . 8 . .
3 . 0 8 . . . 2 .
. . . . 6 0 . . 4
. . . 0 . . 3 . .
4 3 . . . 6 . . 7
7 . 6 . . . . 5 2
```

### Test 4

```
. . . . . . 0 . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . 0 .
. . . . . . . . .
0 . . . . . . . .
. . . 0 . . . . .
. . . . . . . . .
```


