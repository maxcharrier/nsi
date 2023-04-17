def arbre_vide():
	return []


def noeud(etiquette, gauche, droite):
	return [etiquette, gauche, droite]


def etiquette(arbre):
	return arbre[0]


def gauche(arbre):
	return arbre[1]


def droite(arbre):
	return arbre[2]


def est_vide(arbre):
	return arbre == arbre_vide()
