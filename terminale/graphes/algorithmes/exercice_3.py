from graphe_dict import voisins


def parcours_largeur(graphe: dict[str, list[str]], sommet: str):
    """ Parcours sur un graphe en largeur """
    courants = []
    suivants = []
    parcours = []
    courants.append(sommet)
    parcours.append(sommet)
    while courants != []:
        sommet_courant = courants.pop()
        for voisin in voisins(graphe, sommet_courant):
            if voisin not in parcours:
                suivants.append(voisin)
                parcours.append(voisin)
        if courants == []:
            courants = suivants
            suivants = []
    return parcours


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

print(parcours_largeur(graphe1, "b"))
