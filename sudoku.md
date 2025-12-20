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


# Un algithme corrigé et optimisé

Recodage intégral de l'algothme avec un moteur Sudokus repensé.

- Adaptée a toute taille de sudokus
```python
class Sudoku:
    def __init__(self, n):
        self.n = n
        self.s = n * n
        self.grid = [ [None for _ in range(self.s)] for _ in range(self.s) ]
        self.entropies = [ [[i for i in range(self.s)] for _ in range(self.s)] for _ in range(self.s)]
```
- Réduction des entropies optimisé
```python
def place_and_reduce(self, i, j, n):
    self.grid[i][j] = n
    coords = self.box_coords(i, j)
    for k in range(self.s):
        self.entropies[i][k] = reduce(self.entropies[i][k], n)
        self.entropies[k][j] = reduce(self.entropies[k][j], n)
        (x, y) = coords[k]
        self.entropies[x][y] = reduce(self.entropies[x][y], n)
    self.entropies[i][j] = []
```
- Choix aléatoire parmi cases a entropie égale
```python
def wfc_min_entropy(S):
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
            continue
        r = random.randint(0, len(min_entropy_coords) - 1)
        (x, y) = min_entropy_coords[r]
        r2 = random.randint(0, min_entropy - 1)
        el = S.entropies[x][y][r2]
        S.place_and_reduce(x, y, el)
        tag = True

    return not contraditcion
```
- Meilleu affichage
```python
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
```

**Résultat**: Résolution sudoku 9x9 600 fois plus rapide (2.3s vs 0.0036s)!

## Tests
### Comparaison choix entropie minimale/maximale, grille vide
#### Sudokus 4x4

```json
Test: comparaison heuristique choix entropie min/max avec une grille vide
Parametres:
Grilles:            4 x 4
Nombre d'essais:    100000


Version choix de l'entropie minimale
Progrés:            100.%


Le sudoku est resolu 95.333% du temps (95333).
En moyene, wfc resolve 15.78991/16 cases.


Version choix de l'entropie maximale
Progrés:            100.%


Le sudoku est resolu 57.175% du temps (57175).
En moyene, wfc resolve 12.55557/16 cases.
```
#### Sudokus 9x9
```json
Test: comparaison heuristique choix entropie min/max avec une grille vide
Parametres:
Grilles:            9 x 9
Nombre d'essais:    10000


Version choix de l'entropie minimale
Progrés:            100.%


Le sudoku est resolu 56.06% du temps (5606).
En moyene, wfc resolve 64.5301/81 cases.


Version choix de l'entropie maximale
Progrés:            100.%

Le sudoku est resolu 0.02% du temps (2).
En moyene, wfc resolve 33.7432/81 cases.
```

#### Sudokus 16x16

```json
Test: comparaison heuristique choix entropie min/max avec une grille vide
Parametres:
Grilles:            16 x 16
Nombre d'essais:    1000


Version choix de l'entropie minimale
Progrés:            100.%


Le sudoku est resolu 2.5% du temps (25).
En moyene, wfc resolve 97.104/256 cases.


Version choix de l'entropie maximale
Progrés:            100.%


Le sudoku est resolu 0.0% du temps (0).
En moyene, wfc resolve 112.034/256 cases.
```
### Grille peu remplie

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
#### Résultat

```json
Test: comparaison heuristique choix entropie min/max avec une grille vide
Parametres:
Grilles:            9 x 9
Nombre d'essais:    10000


Version choix de l'entropie minimale
Progrés:            100.%


Le sudoku est resolu 56.81% du temps (5681).
En moyene, wfc resolve 66.9731/81 cases.


Version choix de l'entropie maximale
Progrés:            100.%


Le sudoku est resolu 0.0% du temps (0).
En moyene, wfc resolve 33.729/81 cases.
```

questions:
- systeme lineaires: bon ou mauvais modele?
- grille quasi remplie (sauf un bloc): modelisation
