class Arbre():
	arbre_vide = None

	def __init__(self, etiquette = None, gauche = None, droite = None):
		self.__etiquette = etiquette
		self.__gauche = gauche
		self.__droite = droite


	def etiquette(self):
		return self.__etiquette


	def gauche(self):
		return self.__gauche


	def droite(self):
		return self.__droite


	def est_vide(self):
		return self is Arbre.arbre_vide
