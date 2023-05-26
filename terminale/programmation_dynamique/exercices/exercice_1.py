from timeit import timeit

def rendu_monnaie(tab_monnaies: list[int], somme: int) -> int:
    if somme == 0:
        return 0

    minimum = somme + 1
    for i in range(len(tab_monnaies)):
        if tab_monnaies[i] <= somme:
            nb_monnaies = 1 + rendu_monnaie(tab_monnaies, somme - tab_monnaies[i])
            if nb_monnaies < minimum:
                minimum = nb_monnaies
    return minimum


def rendu_monnaie_dyn(tab_monnaies: list[int], somme: int, memoire: list[int]) -> int:
    if somme == 0:
        return 0

    if memoire[somme] > 0:
        return memoire[somme]

    minimum = somme + 1
    for i in range(len(tab_monnaies)):
        if tab_monnaies[i] <= somme:
            nb_monnaies = 1 + rendu_monnaie_dyn(tab_monnaies, somme - tab_monnaies[i], memoire)
            if nb_monnaies < minimum:
                minimum = nb_monnaies
                memoire[somme] = minimum
    return minimum


def rendu_monnaie_dyn_iter(tab_monnaies: list[int], somme: int):
    memoire = [0] * (somme + 1)
    garde = [0] * (somme + 1)
    id_monnaies = 0
    for x in range(1, somme + 1):
        minimum = somme + 1
        for i in range(len(tab_monnaies)):
            if tab_monnaies[i] <= x:
                nb_monnaies = 1 + memoire[x - tab_monnaies[i]]
                if nb_monnaies < minimum:
                    minimum = nb_monnaies
                    id_monnaies = i
        memoire[x] = minimum
        garde[x] = id_monnaies

    x = somme
    monnaies_rendu = []
    while x > 0:
        monnaie = tab_monnaies[garde[x]]
        monnaies_rendu.append(monnaie)
        x -= monnaie

    return memoire[somme], monnaies_rendu


somme = 2749
tab_monnaies = [1, 2, 5, 10, 20, 50, 100, 200]
memoire = [0] * (somme + 1)

"""
r1 = rendu_monnaie(tab_monnaies, somme)
t1 = timeit(
    lambda: rendu_monnaie(tab_monnaies, somme),
    number=10,
    globals=globals()
)
print(f"Récursif : {r1}, temps : {t1:f}s")
"""

"""
r2 = rendu_monnaie_dyn(tab_monnaies, somme, memoire)
t2 = timeit(
    lambda: rendu_monnaie_dyn(tab_monnaies, somme, memoire),
    number=10,
    globals=globals()
)
print(f"Dynamique récursif : {r2}, temps : {t2:f}s")
"""

r3, monnaies_r3 = rendu_monnaie_dyn_iter(tab_monnaies, somme)
t3 = timeit(
    lambda: rendu_monnaie_dyn_iter(tab_monnaies, somme),
    number=10,
    globals=globals()
)
print(f"Dynamique itératif : {r3}, monnaies rendu {monnaies_r3}, temps : {t3:f}s")
