"""
Exercice 6 : POO - matrice d'adjacence
"""

class Graphe:
    """ Graphe avec une matrice d'adjacence. """

    def __init__(self, sommets: list[str]):
        self.__sommets = sommets
        self.__matrice = [[0] * len(sommets) for _ in range(len(sommets))]


    def get_sommets(self):
        """ Renvoie la liste des sommets. """
        return self.__sommets
    

    def get_matrice(self):
        """ Renvoie la matrice. """
        return self.__matrice


    def ajouter_arete(self, sommet1: str, sommet2: str):
        """ Ajouter une arête au graphe. """
        index_sommet1 = self.__sommets.index(sommet1)
        index_sommet2 = self.__sommets.index(sommet2)
        self.__matrice[index_sommet1][index_sommet2] = 1
        self.__matrice[index_sommet2][index_sommet1] = 1


    def existe_arete(self, sommet1: str, sommet2: str) -> int:
        """ Vérifie s'il existe une arête. """
        index_sommet1 = self.__sommets.index(sommet1)
        index_sommet2 = self.__sommets.index(sommet2)
        return self.__matrice[index_sommet1][index_sommet2]


    def voisins(self, sommet: str):
        """ Renvoie les voisins d'un sommet. """
        index_sommet = self.__sommets.index(sommet)
        tab_voisins = []
        for i in range(len(self.__sommets)):
            if self.__matrice[index_sommet][i]:
                tab_voisins.append(self.__sommets[i])
        return tab_voisins


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
    print(graphe1.get_matrice())

    print(graphe1.existe_arete("A", "D"))
    print(graphe1.voisins("A"))
    print(graphe1.voisins("D"))

    chaine1 = ["A", "B", "G", "H", "F", "B"]
    chaine2 = ["C", "F", "H", "G", "B", "F", "E", "D"]
    longueur_chaine1 = longueur_chaine(graphe1, chaine1)
    longueur_chaine2 = longueur_chaine(graphe1, chaine2)
    print(f"Longueur de la chaîne {chaine1}: {longueur_chaine1}")
    print(f"Longueur de la chaîne {chaine2} : {longueur_chaine2}")
