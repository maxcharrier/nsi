from random import randint


class JoueurChoix:
    """ Joueur qui choisit un nombre """

    def __init__(self, nom: str, nMax: int) -> None:
        self.__choix = None
        self.__nom = nom
        self.__nMax = nMax
    

    def choisir_nombre(self):
        self.__choix = randint(0, self.__nMax)
    

    def verifier_proposition(self, nombre: int):
        if self.__choix == nombre:
            return "Gagné"
        elif self.__choix > nombre:
            return "Plus"
        else:
            return "Moins"


class JoueurDeviner:
    """ Joueur qui devine un nombre """

    def __init__(self, nom: str, nMax: int) -> None:
        self.__proposition = None
        self.__nom = nom
        self.__nMax = nMax
        self.__reponse = None
        self.__a = 0 # borne basse
        self.__b = nMax # borne haute
    

    def lire_reponse(self, reponse: str):
        if reponse == "Gagné":
            self.__reponse = "Gagné"
            return self.__reponse
        elif reponse == "Plus":
            self.__reponse = "Plus"
            return self.__reponse
        elif reponse == "Moins":
            self.__reponse = "Moins"
            return self.__reponse
        else:
            return "Erreur dans la lecture de la réponse"
    

    def proposer_nombre(self):
        if self.__proposition == None:
            self.__proposition = randint(self.__a, self.__b)
            return self.__proposition
        elif self.__reponse == "Plus":
            # reduction des intervalles
            self.__a = self.__proposition + 1

            self.__proposition = round((self.__a + self.__b) / 2)
            return self.__proposition
        elif self.__reponse == "Moins":
            # reduction des intervalles
            self.__b = self.__proposition - 1

            self.__proposition = round((self.__a + self.__b) / 2)
            return self.__proposition
        elif self.__reponse == "Gagné":
            return self.__proposition
        else:
            return "Erreur dans la proposition du nombre"


class JeuDeviner:
    """ Simulation du jeu deviner un nombre """

    def __init__(self, nom1: str, nom2: str, nMax: int) -> None:
        self.__nMax = nMax
        self.__joueur1 = JoueurChoix(nom1, nMax)
        self.__joueur2 = JoueurDeviner(nom2, nMax)
        self.__proposition = None
        self.__reponse = None
    

    def lancer_jeu(self):
        self.__joueur1.choisir_nombre()
        print("Le joueur 1 commence par choisir un nombre")

        while self.__reponse != "Gagné":
            print("───────────────────────────")

            self.__proposition = self.__joueur2.proposer_nombre()
            print(f"Le joueur 2 propose : {self.__proposition}")

            self.__reponse = self.__joueur1.verifier_proposition(self.__proposition)
            print(f"Le joueur 1 répond : {self.__reponse}")

            self.__reponse = self.__joueur2.lire_reponse(self.__reponse)
            print(f"Le joueur 2 prend connaissance de la réponse : {self.__reponse}")
