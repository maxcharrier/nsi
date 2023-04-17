def recherche_dichotomie(elm: int, tab: list[int], gauche: int, droite: int):
    if gauche > droite:
        return False
    
    m = (gauche + droite) // 2 # dichotomie
    if tab[m] < elm:
        return recherche_dichotomie(elm, tab, m + 1, droite)
    elif tab[m] > elm:
        return recherche_dichotomie(elm, tab, gauche, m - 1)
    else:
        return True


tab = [2, 7, 8, 10, 11, 15, 16, 20, 25, 30, 32]
print(recherche_dichotomie(13, tab, 0, len(tab) - 1))
