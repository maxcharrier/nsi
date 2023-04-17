# Q1
def pile_vide():
	return []

def pile(valeur, pile):
	return [valeur, pile]

# ajoute un élément dans la pile
def push(valeur, pile):
	return [valeur, pile]

# retirer le premier élement de la pile
def pop(pile):
	return (pile[0], pile[1])

# renvoie la premiere valeur de la pile
def sommet(pile):
	return pile[0]

# vérifie si la pile est vide
def est_vide(pile):
	return pile == pile_vide()

# affiche les éléments de la pile
def afficher(pile):
	copie = pile
	while not est_vide(copie):
		print(sommet(copie), end=", ")
		_, copie = pop(copie)

# inverse les éléments de la pile
def inverser(pile):
	pile_inv = pile_vide()
	copie = pile
	while not est_vide(copie):
		val, copie = pop(copie)
		pile_inv = push(val, pile_inv)
	return pile_inv

# affiche la hauteur de la pile
def taille(pile):
	if est_vide(pile):
		return pile_vide()
	
	copie = pile
	long = 0
	while not est_vide(copie):
		_, copie = pop(copie)
		long += 1
	
	return long

# renvoie le premier élément et le dernier élement de la pile
def borne(pile):
	if est_vide(pile):
		return pile_vide(), pile_vide()
	
	copie = pile
	a = sommet(copie)
	while not est_vide(copie):
		b, copie = pop(copie)
	
	return a, b
