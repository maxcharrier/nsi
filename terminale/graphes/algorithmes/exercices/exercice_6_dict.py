"""
Exercice 6 : POO - dictionnaire
"""

class Graphe:
    """ Graphe avec un dictionnaire. """

    def __init__(self, sommets: list[str]):
        self.__adjacence = {key: [] for key in sommets}

    def get_sommets(self):
        """ Renvoie la liste des sommets. """
        return list(self.__adjacence.keys())


    def ajouter_arete(self, sommet1: str, sommet2: str):
        """ Ajouter une arête au graphe. """
        self.__adjacence[sommet1].append(sommet2)
        self.__adjacence[sommet2].append(sommet1)


    def ajouter_sommet(self, sommet: str):
        """ Ajouter un sommet au graphe. """
        if sommet not in self.__adjacence:
            self.__adjacence[sommet] = []


    def existe_arete(self, sommet1: str, sommet2: str) -> int:
        """ Vérifie s'il existe une arête. """
        return sommet2 in self.__adjacence[sommet1]


    def voisins(self, sommet: str):
        """ Renvoie les voisins d'un sommet. """
        return self.__adjacence[sommet]


def parcours_largeur(graphe: Graphe, sommet: str):
    """ Parcours d'un graphe en largeur. """
    courant = [sommet]
    suivants = []
    parcours = [sommet]
    distances = {sommet : 0}
    while len(courant) > 0:
        sommet_courant = courant.pop()
        for voisin in graphe.voisins(sommet_courant):
            if voisin not in parcours:
                suivants.append(voisin)
                parcours.append(voisin)
                distances[voisin] = distances[sommet_courant] + 1
        if len(courant) == 0:
            courant = suivants
            suivants = []
    return parcours, distances


def distance_sommets(graphe: Graphe, sommet1: str, sommet2: str):
    """ Détermine la distance entre deux sommets. """
    _, distances = parcours_largeur(graphe, sommet1)
    #print(distances)
    return distances[sommet2] if sommet2 in distances else None


def longueur_chaine(graphe: Graphe, tab_sommets: list[str]):
    """ Détermine la longuer d'une chaîne. """
    distance = 0
    for i in range(1, len(tab_sommets)):
        distance += distance_sommets(graphe, tab_sommets[i - 1], tab_sommets[i])

    return distance


if __name__ == "__main__":
    tab_sommets1 = ["A", "B", "C", "D", "E", "F", "G", "H"]
    graphe1 = Graphe(tab_sommets1)
    graphe1.ajouter_arete("A", "B")
    graphe1.ajouter_arete("A", "D")
    graphe1.ajouter_arete("B", "F")
    graphe1.ajouter_arete("B", "G")
    graphe1.ajouter_arete("B", "H")
    graphe1.ajouter_arete("C", "E")
    graphe1.ajouter_arete("C", "F")
    graphe1.ajouter_arete("D", "E")
    graphe1.ajouter_arete("E", "F")
    graphe1.ajouter_arete("E", "H")
    graphe1.ajouter_arete("F", "H")
    graphe1.ajouter_arete("H", "G")

    print(graphe1.get_sommets())

    print(graphe1.existe_arete("A", "D"))
    print(graphe1.voisins("A"))
    print(graphe1.voisins("D"))

    chaine1 = ["A", "B", "G", "H", "F", "B"]
    chaine2 = ["C", "F", "H", "G", "B", "F", "E", "D"]
    longueur_chaine1 = longueur_chaine(graphe1, chaine1)
    longueur_chaine2 = longueur_chaine(graphe1, chaine2)
    print(f"Longueur de la chaîne {chaine1}: {longueur_chaine1}")
    print(f"Longueur de la chaîne {chaine2} : {longueur_chaine2}")
