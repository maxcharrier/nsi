def rendu_monnaie(somme: int, tab_monnaie: list[int]):
    monnaie_rendu = []
    somme_restante = somme
    index = len(tab_monnaie) - 1
    while somme_restante > 0:
        if tab_monnaie[index] <= somme_restante:
            monnaie_rendu.append(tab_monnaie[index])
            somme_restante -= tab_monnaie[index]
        else:
            index -= 1
    return monnaie_rendu


liste1 = [1, 2, 5, 10, 20, 50, 100, 200]
somme1 = 63
print(f"Somme à rendre : {somme1}\nMonnaie(s) rendu : {rendu_monnaie(somme1, liste1)}")

liste2 = [1, 2, 20, 50, 100, 200]
somme2 = 63
print(f"Somme à rendre : {somme2}\nMonnaie(s) rendu : {rendu_monnaie(somme2, liste2)}")
