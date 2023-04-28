import graphe_matrice as gmatrix
import graphe_dict as gdict


def denombrement_matrice(graphe: tuple[list[str], list[list[int]]], sommet_specifique: str):
    """ Dénombrement d'un graphe de type matrice d'adjacence. """
    ordre = len(gmatrix.sommets(graphe))
    degre = len(gmatrix.voisins(graphe, sommet_specifique))

    degre_sommet = {}
    for sommet in gmatrix.sommets(graphe):
        degre_sommet[sommet] = len(gmatrix.voisins(graphe, sommet))

    nb_aretes = 0
    degre_max = ("", 0)
    degre_min = ("", None)
    for sommet, valeur in degre_sommet.items():
        if valeur > degre_max[1]:
            degre_max = (sommet, valeur)
        if degre_min[1] is None or valeur < degre_min[1]:
            degre_min = (sommet, valeur)

        nb_aretes += valeur

    nb_aretes = int(nb_aretes / 2)

    return ordre, degre, nb_aretes, degre_max[0], degre_min[0]


def denombrement_dict(graphe: tuple[list[str], list[list[int]]], sommet_specifique: str):
    """ Dénombrement d'un graphe de type dictionnaire. """
    ordre = len(gdict.sommets(graphe))
    degre = len(gdict.voisins(graphe, sommet_specifique))

    degre_sommet = {}
    for sommet in gdict.sommets(graphe):
        degre_sommet[sommet] = len(gdict.voisins(graphe, sommet))

    nb_aretes = 0
    degre_max = ("", 0)
    degre_min = ("", None)
    for sommet, valeur in degre_sommet.items():
        if valeur > degre_max[1]:
            degre_max = (sommet, valeur)
        if degre_min[1] is None or valeur < degre_min[1]:
            degre_min = (sommet, valeur)

        nb_aretes += valeur

    nb_aretes = int(nb_aretes / 2)

    return ordre, degre, nb_aretes, degre_max[0], degre_min[0]


tab_sommets1 = ["s0", "s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9"]
graphe1 = gmatrix.creer_graphe(tab_sommets1)
gmatrix.ajouter_arete(graphe1, "s0", "s1")
gmatrix.ajouter_arete(graphe1, "s0", "s2")
gmatrix.ajouter_arete(graphe1, "s1", "s2")
gmatrix.ajouter_arete(graphe1, "s1", "s3")
gmatrix.ajouter_arete(graphe1, "s2", "s3")
gmatrix.ajouter_arete(graphe1, "s3", "s4")
gmatrix.ajouter_arete(graphe1, "s3", "s6")
gmatrix.ajouter_arete(graphe1, "s3", "s7")
gmatrix.ajouter_arete(graphe1, "s4", "s5")
gmatrix.ajouter_arete(graphe1, "s5", "s6")
gmatrix.ajouter_arete(graphe1, "s7", "s8")
gmatrix.ajouter_arete(graphe1, "s7", "s9")
gmatrix.ajouter_arete(graphe1, "s8", "s9")

ordre, degre, nb_aretes, degre_max, degre_min = denombrement_matrice(graphe1, "s7")
print(f"Ordre du graphe : {ordre}")
print(f"Degré du sommet s7 : {degre}")
print(f"Nombre d'arêtes : {nb_aretes}")
print(f"Sommet de degré le plus élevé : {degre_max}")
print(f"Sommet de degré le plus faible : {degre_min}")


print("------------------------------------------------------------")


tab_sommets2 = ["s0", "s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9"]
graphe2 = gdict.creer_graphe(tab_sommets2)
gdict.ajouter_arete(graphe2, "s0", "s1")
gdict.ajouter_arete(graphe2, "s0", "s2")
gdict.ajouter_arete(graphe2, "s1", "s2")
gdict.ajouter_arete(graphe2, "s1", "s3")
gdict.ajouter_arete(graphe2, "s2", "s3")
gdict.ajouter_arete(graphe2, "s3", "s4")
gdict.ajouter_arete(graphe2, "s3", "s6")
gdict.ajouter_arete(graphe2, "s3", "s7")
gdict.ajouter_arete(graphe2, "s4", "s5")
gdict.ajouter_arete(graphe2, "s5", "s6")
gdict.ajouter_arete(graphe2, "s7", "s8")
gdict.ajouter_arete(graphe2, "s7", "s9")
gdict.ajouter_arete(graphe2, "s8", "s9")

ordre, degre, nb_aretes, degre_max, degre_min = denombrement_dict(graphe2, "s7")
print(f"Ordre du graphe : {ordre}")
print(f"Degré du sommet s7 : {degre}")
print(f"Nombre d'arêtes : {nb_aretes}")
print(f"Sommet de degré le plus élevé : {degre_max}")
print(f"Sommet de degré le plus faible : {degre_min}")
