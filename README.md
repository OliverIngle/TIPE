# Étude de l'algotithme Wave Function Collapse (wfc)

Nombreux jeux (vidéos) d'aventure on besoin de **générer de vastes terrains** pour créer un univers dans lequel les personnages peuvent se déplacer. Des algorithmes de "bruit" tel que le perlin noise et les algorithmes dit d'érosion permettent bien de réaliser cette tache.

Cependant, lorsque les jeux ont plus de **contraintes**, ces algorithmes sont parfois insuffisant.

De ce probleme est née **wfc**: un algorithme qui permet de générer des terrains en prenant en compte des containtes multiples, tout en conservant un aspec aléatoire.

## Positionement thématique

- Informatique (Algorithmeique)
- Informatique (Graphisme)
- Mathématique (Probabilités?)

## Mot clefs

- Génération prcédurale

## Principe de l'algorithme wfc

1. On initialse une grille (2D, ou 3D en fonction du type de terrain a générer) ou toute les cases contiennent une **"superpotition"** de toute les valeurs possibles. Le nombre de valeurs possibles pour une case est appelé son **entropie**.
2. On **"réduit"** (= on choisit une valeur) d'une première case.
3. A partir des containtes, on recalcule l'entropie des autres cases: suite a la modification, certains états ne seront plus possibles pour certaines cases.
4. On choisit une nouvelle case a réduire. Deux méthodes:
- On choisit l'entropie minimale: cases les plus "certaines"
- On chisit l'entropie maximale: diminue plus l'entropie totale (cf plus tard)
On choisit (aléatoirement) une des valeurs possibles pour cette case.
5. On reviens a l'étape **3**.

Il peut arriver qu'il y ai trop de contraintes sur une case et donc pas d'état possible pour celle ci (entropie nulle): c'est une **"contradiction"**.
On peut:
- Arreter l'algorithme et recomencer.
- mettren en place un autre algorithme (ex: backtracking) pour défaire la contradiction.

L'algorithme wfc a une grande souplesse: il s'applique a nombreux scénarions.

# Problématique retenue

N/A

# Objectif du TIPE du condidat

- Implémenter l'algorithme wfc a des situations de complexité croissante. On pourra aboutir avec un générteur de labyrinthes.

- Jouer avec les parametres de l'algorithme (ex: heuristique entropie maximale/minimale) afin de l'optimiser a la situation en question.


## Resources

- [mxgmn: WaveFunctionCollapse - GitHub (Inventeur original)](https://github.com/mxgmn/WaveFunctionCollapse)
- [Wikipedia - Model Synthesis](https://en.wikipedia.org/wiki/Model_synthesis)
- [Une autres description](https://robertheaton.com/2018/12/17/wavefunction-collapse-algorithm/)

## DOT

- Avril - Juin 2024: Première implémentation de wfc: Résolution et génération de sudokus.
