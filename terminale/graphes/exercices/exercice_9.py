from pprint import pprint


def creer_graphe(sommets):
    dimension = len(sommets)
    matrice = [[0 for i in range(dimension)] for j in range(dimension)]
    return (sommets, matrice)


def ajouter_arete(graphe, sommet1, sommet2):
    sommets = graphe[0]
    i = sommets.index(sommet1)
    j = sommets.index(sommet2)
    matrice = graphe[1]
    matrice[i][j] = 1
    matrice[j][i] = 1
    return graphe


def sommets(graphe):
    return graphe[0]


def voisins(graphe, sommet):
    sommets = graphe[0]
    matrice = graphe[1]
    i = sommets.index(sommet)
    voisins = []
    for j in range(len(matrice[i])):
        if matrice[i][j] == 1:
            voisins.append(sommets[j])
    return voisins

# -----------------
# GRAPHE 1
# -----------------
print("\nGRAPHE 1")
tab1 = ["a", "b", "c", "d", "e", "f", "g", "h"]
graphe1 = creer_graphe(tab1)
ajouter_arete(graphe1, "a", "b")
ajouter_arete(graphe1, "a", "d")
ajouter_arete(graphe1, "a", "e")
ajouter_arete(graphe1, "b", "c")
ajouter_arete(graphe1, "c", "d")
ajouter_arete(graphe1, "d", "e")
ajouter_arete(graphe1, "e", "f")
ajouter_arete(graphe1, "e", "g")
ajouter_arete(graphe1, "f", "g")
ajouter_arete(graphe1, "g", "h")

pprint(graphe1, width=50)

print(f"Voisin(s) de A : {voisins(graphe1, 'a')}")
print(f"Voisin(s) de E : {voisins(graphe1, 'e')}")
print(f"Voisin(s) de H : {voisins(graphe1, 'h')}")


# -----------------
# GRAPHE 2
# -----------------
print("\nGRAPHE 2")
tab_sommets = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
matrice = [
#    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0]
]
graphe2 = (tab_sommets, matrice)

pprint(graphe2, width=50)

print(f"Voisin(s) de 2 : {voisins(graphe2, '2')}")
print(f"Voisin(s) de 9 : {voisins(graphe2, '9')}")

def afficher_tous_voisins(graphe):
    for sommet in sommets(graphe2):
        print(f"Voisin(s) de {sommet} : {voisins(graphe2, sommet)}")
afficher_tous_voisins(graphe2)
