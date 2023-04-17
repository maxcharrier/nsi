def inverser(chaine: str) -> str:
    if len(chaine) == 1: # Cas de base
        return chaine
    else: # Cas général
        return inverser(chaine[1:]) + chaine[0]

def main():
    r = inverser("Python")
    print(r)

if __name__ == "__main__":
    main()
