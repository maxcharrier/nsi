class Cellule():
	""" Structure d'une cellule """

	def __init__(self, val: int, suiv = None):
		self.valeur = val
		self.suivante = suiv

class Pile():
	""" Structure d'une pile """

	def __init__(self):
		self.contenue = None # cellule
		self.long = 0 # hauteur de la pile
	

	def est_vide(self):
		""" Vérifie si la pile est vide """
		return self.contenue is None
	
	
	def push(self, val: int):
		""" Ajoute un élement dans la pile """
		self.contenue = Cellule(val, self.contenue)
		self.long += 1


	def pop(self):
		""" Retirer le dernier élément de la pile et le renvoie """
		if self.est_vide():
			raise IndexError("La pile est vide !")
		
		val = self.contenue.valeur
		self.pile = self.contenue.suivante

		self.long -= 1

		return val


	def afficher(self):
		""" Affiche les éléments de la pile """
		cel = self.contenue
		while cel is not None:
			print(cel.valeur, end="; ")
			cel = cel.suivante
		print()
	

	def taille(self):
		""" Afficher la hauteur de la pile """
		return self.long
	
	
	def inserer(self, elm: int, pos: int):
		""" Insère un élément à une certaine position dans la pile """
		if self.est_vide():
			raise IndexError("La pile est vide !")

		cel = self.contenue
		nouvelle_cel = Cellule(elm)
		
		# itérer sur les positions jusqu'à avant notre position voulue
		n = 0
		while n < pos - 1:
			cel = cel.suivante
			n += 1
		
		# decaler les cellules et inserer la nouvelle cellule
		nouvelle_cel.suivante = cel.suivante
		cel.suivante = nouvelle_cel

		self.long += 1
