from pprint import pprint


def creer_graphe(sommets: list[str]):
    return {key: [] for key in sommets}


def ajouter_arete(graphe: dict[str, list[str]], sommet1: str, sommet2: str):
    graphe[sommet1].append(sommet2)
    graphe[sommet2].append(sommet1)


def sommets(graphe: dict[str, list[str]]):
    return list(graphe.keys())


def voisins(graphe: dict[str, list[str]], sommet: str):
    return graphe[sommet]


# -----------------
# GRAPHE 1
# -----------------
print("\nGRAPHE 1")
tab1 = ["a", "b", "c", "d", "e", "f", "g", "h"]
graphe1 = creer_graphe(tab1)
ajouter_arete(graphe1, "a", "b")
ajouter_arete(graphe1, "a", "d")
ajouter_arete(graphe1, "a", "e")
ajouter_arete(graphe1, "b", "a")
ajouter_arete(graphe1, "b", "c")
ajouter_arete(graphe1, "c", "b")
ajouter_arete(graphe1, "c", "d")
ajouter_arete(graphe1, "d", "a")
ajouter_arete(graphe1, "d", "c")
ajouter_arete(graphe1, "d", "e")
ajouter_arete(graphe1, "e", "a")
ajouter_arete(graphe1, "e", "d")
ajouter_arete(graphe1, "e", "f")
ajouter_arete(graphe1, "e", "g")
ajouter_arete(graphe1, "f", "e")
ajouter_arete(graphe1, "f", "g")
ajouter_arete(graphe1, "g", "e")
ajouter_arete(graphe1, "g", "f")
ajouter_arete(graphe1, "g", "h")
ajouter_arete(graphe1, "h", "g")

pprint(graphe1, width=30)

print(f"Voisin(s) de E : {voisins(graphe1, 'e')}")
print(f"Voisin(s) de H : {voisins(graphe1, 'h')}")

# -----------------
# GRAPHE 2
# -----------------
print("\nGRAPHE 2")
graphe2 = {
    "1": ["3", "4", "5"],
    "2": ["5", "7"],
    "3": ["1", "4"],
    "4": ["1", "3", "7"],
    "5": ["1", "2", "9", "10"],
    "6": ["7", "8", "9"],
    "7": ["2", "4", "6", "8"],
    "8": ["6", "7"],
    "9": ["5", "6", "10", "11"],
    "10": ["5", "9", "11"],
    "11": ["9", "10"]
}

pprint(graphe2, width=30)

print(f"Voisin(s) de 2 : {graphe2['2']}")
print(f"Voisin(s) de 9 : {graphe2['9']}")

# -----------------
# GRAPHE 3
# -----------------
print("\nGRAPHE 3")
tab3 = ["a", "b", "c", "d", "e", "f", "g", "h"]
graphe3 = creer_graphe(tab3)
ajouter_arete(graphe3, "a", "b")
ajouter_arete(graphe3, "a", "d")
ajouter_arete(graphe3, "a", "e")
ajouter_arete(graphe3, "b", "a")
ajouter_arete(graphe3, "b", "c")
ajouter_arete(graphe3, "c", "b")
ajouter_arete(graphe3, "c", "d")
ajouter_arete(graphe3, "d", "a")
ajouter_arete(graphe3, "d", "c")
ajouter_arete(graphe3, "d", "e")
ajouter_arete(graphe3, "e", "a")
ajouter_arete(graphe3, "e", "d")
ajouter_arete(graphe3, "e", "f")
ajouter_arete(graphe3, "e", "g")
ajouter_arete(graphe3, "f", "e")
ajouter_arete(graphe3, "f", "g")
ajouter_arete(graphe3, "g", "e")
ajouter_arete(graphe3, "g", "f")
ajouter_arete(graphe3, "g", "h")
ajouter_arete(graphe3, "h", "g")

pprint(graphe3, width=30)

# -----------------
# GRAPHE 4
# -----------------
print("\nGRAPHE 4")
graphe4 = {
    "1": ["3", "4", "5"],
    "2": ["5", "7"],
    "3": ["1", "4"],
    "4": ["1", "3", "7"],
    "5": ["1", "2", "9", "10"],
    "6": ["7", "8", "9"],
    "7": ["2", "4", "6", "8"],
    "8": ["6", "7"],
    "9": ["5", "6", "10", "11"],
    "10": ["5", "9", "11"],
    "11": ["9", "10"]
}

pprint(graphe4, width=30)