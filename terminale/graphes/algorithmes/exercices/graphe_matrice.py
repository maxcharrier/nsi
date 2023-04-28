def creer_graphe(tab_sommets: list[str]):
    """ Créer un graphe en utilisant une matrice d'adjacence. """
    dimension = len(tab_sommets)
    matrice = [[0 for _ in range(dimension)] for _ in range(dimension)]
    return (tab_sommets, matrice)


def ajouter_arete(
        graphe: tuple[list[str], list[list[int]]],
        sommet1: str,
        sommet2: str
    ):
    """ Ajouter une arête au graphe. """
    tab_sommets = graphe[0]
    matrice = graphe[1]
    i = tab_sommets.index(sommet1)
    j = tab_sommets.index(sommet2)
    matrice[i][j] = 1
    matrice[j][i] = 1
    return graphe


def sommets(graphe: tuple[list[str], list[list[int]]]):
    """ Renvoie la liste des sommets. """
    return graphe[0]


def voisins(graphe: tuple[list[str], list[list[int]]], sommet: str):
    """ Renvoie les voisins d'un sommet. """
    tab_sommets = graphe[0]
    matrice = graphe[1]
    i = tab_sommets.index(sommet)
    tab_voisins = []
    for j in range(len(matrice[i])):
        if matrice[i][j] == 1:
            tab_voisins.append(tab_sommets[j])
    return tab_voisins
