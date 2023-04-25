from graphe_dict import sommets, voisins


def parcours_profondeur(graphe: dict[str, list[str]], vus: list[str], sommet: str):
    """ Parcours sur un graphe en profondeur """
    pile = []
    pile.append(sommet)
    while pile != []:
        sommet = pile.pop()
        if sommet not in vus:
            vus.append(sommet)
            for voisin in voisins(graphe, sommet):
                pile.append(voisin)
    return vus


def existe_chaine(graphe: dict[str, list[str]], sommet1: str, sommet2: str):
    """ Renvoie s'il existe une chaine entre deux sommets """
    return sommet2 in parcours_profondeur(graphe, [], sommet1)



def est_connexe(graphe: dict[str, list[str]]):
    """ Renvoie si le graphe est connexe """
    tab_sommets = sommets(graphe)
    parcours = parcours_profondeur(graphe, [], tab_sommets[0])
    return len(tab_sommets) == len(parcours)


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

tab_sommets = sommets(graphe2)
for sommet1 in tab_sommets:
    for sommet2 in tab_sommets:
        if sommet1 == sommet2:
            continue
        r = existe_chaine(graphe2, sommet1, sommet2)
        print(f"{sommet1} {sommet2} ==> {r}")


print(est_connexe(graphe1)) # True
print(est_connexe(graphe2)) # False
