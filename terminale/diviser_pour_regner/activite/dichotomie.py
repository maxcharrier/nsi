def recherche_dichotomie(x: int, tab: list):
    a = 0 # borne gauche
    b = len(tab) - 1 # borne droite
    while a <= b:
        m = (a + b) // 2 # dichotomie
        if tab[m] == x:
            # x trouvé
            return True
        elif tab[m] < x:
			# x inférieur
            a = m + 1
        else:
			# x supérieur
            b = m - 1
    # on a a > b
    return False


def test_dichotomie(tab: list):
	for elm in tab:
		r = recherche_dichotomie(elm, tab)
		print(f"{elm} {r}")
	
	for elm in [min(tab) - 1, max(tab) + 1]:
		r = recherche_dichotomie(elm, tab)
		print(f"{elm} {r}")

tab = [1, 5, 6, 8, 9, 15, 16, 20, 25]
x = 15

print(recherche_dichotomie(x, tab))

test_dichotomie(tab)
