class Cellule():
    """ Structure d'une cellule """

    def __init__(self, val: int, suiv = None):
        self.valeur = val
        self.suivante = suiv


class Liste():
    """ Structure d'une liste chainée """

    def __init__(self):
        self.tete = None
        self.long = 0

        
    def est_vide(self):
        """ Vérifie si la liste est vide """
        return self.tete is None
    

    def ajouter(self, val: int):
        """ Ajoute une valeur dans la liste """
        self.tete = Cellule(val, self.tete)
        self.long += 1
    

    def afficher(self):
        """ Affiche tout les éléments de la liste """
        if self.est_vide():
            return None
        
        cel = self.tete
        while cel is not None:
            print(cel.valeur, end=", ")
            cel = cel.suivante
    

    def taille(self):
        """ Renvoie le nombre d'éléments de la liste """
        return self.long


    def inserer(self, elm: int, pos: int):
        """ Insère un élément à une certaine position """
        cel = self.tete
        ncel = Cellule(elm)
        self.long += 1
        n = 0
        while n < pos - 1:
            cel = cel.suivante
            n += 1
        ncel.suivante = cel.suivante
        cel.suivante = ncel
