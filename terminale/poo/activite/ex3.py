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

def main():
    velo1 = Velo()

    velo1.avancer(5)
    r = velo1.obtenir_pos()
    print(r)

if __name__ == "__main__":
    main()
