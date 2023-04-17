def lapins(mois: int) -> int:
    if mois == 1 or mois == 2: # Cas de base
        return 1
    else: # Cas général
        return lapins(mois - 1) + lapins(mois - 2)

def lapins2(mois: int) -> int:
    if mois == 1 or mois == 2: # Cas de base
        return 1
    else: # Cas général
        vi = lapins2(mois - 1)
        vf = vi + lapins2(mois - 2)
        t = (vf - vi) / vi
        print(t)

        return vf

def main():
    #r = lapins(10)
    #print(r)
    lapins2(10)

if __name__ == "__main__":
    main()
