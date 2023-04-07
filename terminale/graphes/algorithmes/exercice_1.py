from graphe_dict import voisins


def parcours_profondeur(graphe: dict[str, list[str]], vus: list[str], sommet: str):
    """ Parcours sur un graphe en profondeur """
    if sommet not in vus:
        vus.append(sommet)
        for voisin in voisins(graphe, sommet):
            parcours_profondeur(graphe, vus, voisin)
    return vus


def existe_chaine(graphe: dict[str, list[str]], sommet1: str, sommet2: str):
    """ Renvoie s'il existe une chaine entre deux sommets """
    return sommet2 in parcours_profondeur(graphe, [], sommet1)


graphe1 = {
    "a" : ["b","c"],
    "b" : ["a", "d", "e"],
    "c" : ["a", "d"],
    "d" : ["b", "c", "e"],
    "e" : ["b", "d", "f", "g"],
    "f" : ["e", "g"],
    "g" : ["e", "f", "h"],
    "h" : ["g"]
}

graphe2 = {
    "A": ["B"],
    "B": ["A", "C"],
    "C": ["B"],
    "D": ["E"],
    "E": ["D"]
}

print(parcours_profondeur(graphe1, [], "g"))

print(existe_chaine(graphe1, "g", "d")) # True
print(existe_chaine(graphe2, "A", "D")) # False
