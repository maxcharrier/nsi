import graphe_matrice as gmatrix


def parcours_largeur(graphe: dict[str, list[str]], sommet: str):
    """ Parcours d'un graphe en largeur. """
    courant = [sommet]
    suivants = []
    parcours = [sommet]
    distances = {sommet : 0}
    while len(courant) > 0:
        sommet_courant = courant.pop()
        for voisin in gmatrix.voisins(graphe, sommet_courant):
            if voisin not in parcours:
                suivants.append(voisin)
                parcours.append(voisin)
                distances[voisin] = distances[sommet_courant] + 1
        if len(courant) == 0:
            courant = suivants
            suivants = []
    return parcours, distances


def distance_sommets(graphe: dict[str, list[str]], sommet1: str, sommet2: str):
    """ Détermine la distance entre deux sommets. """
    _, distances = parcours_largeur(graphe, sommet1)
    #print(distances)
    return distances[sommet2] if sommet2 in distances else None


def longueur_chaine(graphe: tuple[list[str], list[list[int]]], tab_sommets: list[str]):
    """ Détermine la longuer d'une chaîne. """
    distance = 0
    for i in range(1, len(tab_sommets)):
        distance += distance_sommets(graphe, tab_sommets[i - 1], tab_sommets[i])

    return distance


tab_sommets1 = ["A", "B", "C", "D", "E", "F", "G", "H"]
graphe1 = gmatrix.creer_graphe(tab_sommets1)
gmatrix.ajouter_arete(graphe1, "A", "B")
gmatrix.ajouter_arete(graphe1, "A", "D")
gmatrix.ajouter_arete(graphe1, "B", "F")
gmatrix.ajouter_arete(graphe1, "B", "G")
gmatrix.ajouter_arete(graphe1, "B", "H")
gmatrix.ajouter_arete(graphe1, "C", "E")
gmatrix.ajouter_arete(graphe1, "C", "F")
gmatrix.ajouter_arete(graphe1, "D", "E")
gmatrix.ajouter_arete(graphe1, "E", "F")
gmatrix.ajouter_arete(graphe1, "E", "H")
gmatrix.ajouter_arete(graphe1, "F", "H")
gmatrix.ajouter_arete(graphe1, "H", "G")

chaine1 = ["A", "B", "G", "H", "F", "B"]
chaine2 = ["C", "F", "H", "G", "B", "F", "E", "D"]
longueur_chaine1 = longueur_chaine(graphe1, chaine1)
longueur_chaine2 = longueur_chaine(graphe1, chaine2)
print(f"Longueur de la chaîne {chaine1}: {longueur_chaine1}")
print(f"Longueur de la chaîne {chaine2} : {longueur_chaine2}")
