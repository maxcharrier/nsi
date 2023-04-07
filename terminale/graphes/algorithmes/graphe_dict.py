def creer_graphe(tab_sommets: list[str]):
    """ Créer un graphe en utilisant un dictionnaire """
    return {key: [] for key in tab_sommets}


def ajouter_arete(graphe: dict[str, list[str]], sommet1: str, sommet2: str):
    """ Ajouter une arete entre deux sommets """
    graphe[sommet1].append(sommet2)
    graphe[sommet2].append(sommet1)


def sommets(graphe: dict[str, list[str]]):
    """ Renvoie la liste des sommets """
    return list(graphe.keys())


def voisins(graphe: dict[str, list[str]], sommet: str):
    """ Renvoie les voisins d'un sommet """
    return graphe[sommet]
