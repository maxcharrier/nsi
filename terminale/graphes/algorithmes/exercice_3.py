from graphe_dict import voisins


def parcours_largeur(graphe: dict[str, list[str]], sommet: str):
    """ Parcours d'un graphe en largeur. """
    courant = [sommet]
    suivants = []
    parcours = [sommet]
    distances = {sommet : 0}
    while len(courant) > 0:
        sommet_courant = courant.pop()
        for voisin in voisins(graphe, sommet_courant):
            if voisin not in parcours:
                suivants.append(voisin)
                parcours.append(voisin)
                distances[voisin] = distances[sommet_courant] + 1
        if len(courant) == 0:
            courant = suivants
            suivants = []
    return parcours, distances


def distance(graphe: dict[str, list[str]], sommet1: str, sommet2: str):
    """ Détermine la distance entre deux sommets. """
    _, distances = parcours_largeur(graphe, sommet1)
    print(distances)
    return distances[sommet2] if sommet2 in distances else None


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

parcours_graphe, _ = parcours_largeur(graphe1, "b")
print(parcours_graphe)

print(distance(graphe1, "a", "h"))
