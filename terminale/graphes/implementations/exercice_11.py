from pprint import pprint


def creer_graphe(sommets: list[str]):
    """
    Créer un graphe en utilisant une matrice d'adjacence.
    """
    dimension = len(sommets)
    matrice = [[None for _ in range(dimension)] for _ in range(dimension)]
    return (sommets, matrice)


def ajouter_arete(
        graphe: tuple[list[str], list[list[None]]],
        sommet1: str,
        sommet2: str,
        poids: int | list[int]
    ):
    """
    Ajouter une arête (connexion entre deux sommets) au graphe.
    """
    sommets = graphe[0]
    matrice = graphe[1]
    i = sommets.index(sommet1)
    j = sommets.index(sommet2)
    matrice[i][j] = poids
    return graphe


def tab_sommets(graphe: tuple[list[str], list[list[None]]]):
    """
    Renvoie le tableau des sommets.
    """
    return graphe[0]


def voisins(graphe: tuple[list[str], list[list[None]]], sommet: str):
    """
    Afficher les voisins d'un sommet.
    """
    sommets = graphe[0]
    matrice = graphe[1]
    i = sommets.index(sommet)
    tab_voisins = []
    for j in range(len(matrice[i])):
        if matrice[i][j] is not None:
            tab_voisins.append(sommets[j])
    return tab_voisins


tab1 = ["a", "b", "c", "d", "e", "f"]
graphe1 = creer_graphe(tab1)
ajouter_arete(graphe1, "a", "a", 7)
ajouter_arete(graphe1, "a", "b", 1)
ajouter_arete(graphe1, "a", "e", 2)
ajouter_arete(graphe1, "b", "c", [3, 8])
ajouter_arete(graphe1, "b", "f", 4)
ajouter_arete(graphe1, "e", "f", 5)
ajouter_arete(graphe1, "f", "e", 6)

pprint(graphe1)

for sommet in tab_sommets(graphe1):
    print(f"Voisin(s) de {sommet} : {voisins(graphe1, sommet)}")
