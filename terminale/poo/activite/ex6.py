class Velo:
    def __init__(self, roues: int, pos: int) -> None:
        self.__couleur = "Rouge"
        self.__roues = 2
        self.__pos = 0
    
    def _obtenir_pos(self) -> int:
        return self.__pos
    
    def _modifier_pos(self, value: int) -> None:
        self.__pos = value
    
    def _avancer(self, value: int) -> None:
        self.__pos += value

class VeloElectrique(Velo):
    def __init__(self, roues: int, pos: int) -> None:
        super().__init__(roues, pos)
        self.__couleur = "Rouge"
        self.__autonomie = 50

    def _get_autonomie(self):
        return self.__autonomie
    
    def _set_autonomie(self, value: int):
        self.__autonomie = value
    
    def afficher_type(self):
        print("Je suis un vélo électrique")

def main():
    velo1 = Velo(2, 0)
    veloE = VeloElectrique(3, 0)

    print(dir(veloE))

    print(veloE._get_autonomie())
    
    veloE._avancer(5)
    veloE._avancer(6)
    print(veloE._obtenir_pos())

    veloE.afficher_type()

    print(velo1._obtenir_pos())

if __name__ == "__main__":
    main()
