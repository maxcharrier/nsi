class Cellule():
	""" Structure d'une cellule """

	def __init__(self, val: int, suiv = None):
		self.valeur = val
		self.suivante = suiv

class File():
	""" Structure d'une file """

	def __init__(self):
		self.tete = None # premier elemnt de la file
		self.queue = None # dernier element de la file
		self.long = 0 # longueur de la file
	

	def est_vide(self):
		""" Vérifie si la file est vide """
		return self.tete is None
	

	def push(self, val: int):
		""" Ajoute une valeur dans la file """
		cel = Cellule(val, None)
		if self.est_vide():
			self.tete = cel
		else:
			self.queue.suivante = cel
		self.queue = cel
		self.long += 1
	
	def pop(self):
		""" Retire le premier élement de la file et le renvoie """
		if self.est_vide():
			raise IndexError("La file est vide !")
		
		val = self.tete.valeur
		self.tete = self.tete.suivante
		self.long -= 1

		return val
	

	def afficher(self):
		""" Affiche les éléments de la file """
		if self.est_vide():
			return None
		
		cel = self.tete
		while cel is not None:
			print(cel.valeur, end=", ")
			cel = cel.suivante
		print()
	
	
	def taille(self):
		""" Affiche la longueur de la file """
		return self.long
