from random import randint
from typing import List

class Puce:
    """ Gestion logique d'une puce """
    
    def __init__(self, nom: str, couleur: str, pos: int) -> None:
        self.__nom = nom
        self.__couleur = couleur
        self.__pos = pos
    
    # obtenir nom de la puce
    def get_nom(self):
        return self.__nom
    
    # obteneir couleur de la puce
    def get_couleur(self):
        return self.__couleur
    
    # obtenir position de la puce
    def get_position(self):
        return self.__pos
    
    # définir position de la puce
    def set_position(self, value: int):
        self.__pos = value
        return self.get_position()
    
    # faire avancer la puce
    def avancer(self):
        self.__pos += randint(1, 3)
        return self.get_position()

class Course:
    """ Simulation d'une course """

    def __init__(self, taille: int) -> None:
        self.__taille = taille
        self.__puces: List[Puce] = []
    
    # ajout des puces
    def ajouter_puce(self, puce: Puce):
        self.__puces.append(puce)
    
    # obtenir toutes les puces présentes à la course
    def get_puces(self):
        return self.__puces
    
    # jouer la course !
    def deplacer_puces(self):
        positions_puces: List[List[Puce, int]] = []

        for puce in self.__puces:
            positions_puces.append([puce, puce.avancer()])

            print(f"{puce.get_nom()} est en position : {puce.get_position()}")

            if puce.get_position() >= self.__taille:
                print(f"{puce.get_nom()} est arrivée")
        
        return positions_puces
