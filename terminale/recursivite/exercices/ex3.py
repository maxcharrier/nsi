def somme(liste: int) -> int:
    if len(liste) == 1: # Cas de base
        return liste[0]
    else: # Cas général
        a = liste.pop()
        return a + somme(liste)

def main():
    liste1 = [3, 7, 5, 10, 8]

    r = somme(liste1)
    print(r)

if __name__ == "__main__":
    main()
