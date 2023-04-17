class Velo:
    def __init__(self) -> None:
        self.couleur = "Rouge"
        self.roues = 2

def main():
    velo1 = Velo()
    velo2 = Velo()

    print(velo1.couleur)
    print(velo2.couleur)
    print(velo1.roues)
    print(velo2.roues)

    print(velo1 == velo2)

    velo1.couleur = "Vert"
    velo2.roues = 3
    
    print(velo1.couleur)
    print(velo2.couleur)
    print(velo1.roues)
    print(velo2.roues)

if __name__ == "__main__":
    main()
