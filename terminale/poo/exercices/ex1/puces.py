from random import randint
from typing import List

class Puce:
    def __init__(self, nom: str, couleur: str, pos: int) -> None:
        self.__nom = nom
        self.__couleur = couleur
        self.__pos = pos
    
    def get_nom(self):
        return self.__nom
    
    def get_couleur(self):
        return self.__couleur
    
    def get_position(self):
        return self.__pos
    
    def set_position(self, value: int):
        self.__pos = value
        return self.get_position()
    
    def avancer(self):
        self.__pos += randint(1, 3)
        return self.get_position()

class Course:
    """Simulation d'une course"""

    def __init__(self, taille: int) -> None:
        self.__taile = taille
        self.__puces: List[Puce] = []
    
    def ajouter_puce(self, puce: Puce):
        self.__puces.append(puce)
    
    def deplacer_puces(self):
        print("───────────────────────────")
        
        for puce in self.__puces:
            puce.avancer()

            print(f"{puce.get_nom()} est en position : {puce.get_position()}")

            if puce.get_position() >= 10:
                print(f"{puce.get_nom()} est arrivée")
