class Velo:
    def __init__(self) -> None:
        self.couleur = "Rouge"
        self._roues = 2
        self.__pos = 0

def main():
    mon_velo = Velo()

    print(mon_velo.couleur)
    print(mon_velo._roues)
    print(mon_velo.__pos)

if __name__ == "__main__":
    main()
