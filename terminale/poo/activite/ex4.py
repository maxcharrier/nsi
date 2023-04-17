class Velo:
    def __init__(self) -> None:
        self.__couleur = "Rouge"
        self.__roues = 2
        self.__pos = 0
    
    def obtenir_pos(self) -> int:
        return self.__pos
    
    def modifier_pos(self, value: int) -> None:
        self.__pos = value
    
    def avancer(self, value: int) -> None:
        self.__pos += value
    
    pos = property(obtenir_pos, modifier_pos)

def main():
    velo1 = Velo()

    print(velo1.pos)
    velo1.pos = 15
    print(velo1.pos)

    velo1.avancer(5)
    velo1.avancer(6)

    print(velo1.pos)

if __name__ == "__main__":
    main()
