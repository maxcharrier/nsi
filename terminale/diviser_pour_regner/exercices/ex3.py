import matplotlib.pyplot as plt
from random import randint
from timeit import timeit


def fusion(tab1: list, tab2: list):
    resultat = []
    pos1, pos2 = 0, 0
    
    while pos1 < len(tab1) and pos2 < len(tab2):
        if tab1[pos1] < tab2[pos2]:
            resultat.append(tab1[pos1])
            pos1 += 1
        else:
            resultat.append(tab2[pos2])
            pos2 += 1
    
    if pos1 < len(tab1):
        resultat += tab1[pos1:]
    else:
        resultat +=tab2[pos2:]
    
    return resultat


def tri_fusion(tab: list):
    n = len(tab)
    
    if n <= 1: # cas de base
        return tab
    else:
        # diviser
        tab1 = tab[:n//2]
        tab2 = tab[n//2:]
        #print(f"Diviser {tab1}{tab2}")

        # regner
        tab1_trie = tri_fusion(tab1)
        tab2_trie = tri_fusion(tab2)
        #print(f"Régner {tab1_trie}{tab2_trie}")

        # combiner
        resultat = fusion(tab1_trie, tab2_trie)
        #print(f"Combiner {resultat}")
        
        return resultat


def tri_insertion(tab: list):
    n = len(tab)
    
    for i in range(1, n): 
        elm = tab[i] # élément en cours
        j = i # second index

        # décalage des éléments du tableau
        while j > 0 and tab[j-1] > elm: 
                tab[j] = tab[j-1] 
                j -= 1
        
        # insertion
        tab[j] = elm


def tri_selection(tab: list):
    n = len(tab)

    for i in range(n):
        minimum = i # élément en cours

        for j in range(i+1, n):
            if tab[j] < tab[minimum]:
                minimum = j
                
        tmp = tab[i]
        tab[i] = tab[minimum]
        tab[minimum] = tmp

tab1 = [10, 4, 12, 23, 32, 35, 42, 56, 57]


def tracer_courbe(n_max = 10):
    liste_x = []
    liste_y1 = []
    liste_y2 = []
    liste_y3 = []

    for n in range(n_max):
        # Tableau des abscisses
        tab = [randint(0, 100) for _ in range(n)]
        liste_x.append(n)

        # Tableau des ordonnées
        time1 = timeit(lambda: tri_fusion(tab), number=100, globals=globals())
        liste_y1.append(time1)

        time2 = timeit(lambda: tri_insertion(tab), number=100, globals=globals())
        liste_y2.append(time2)

        time3 = timeit(lambda: tri_selection(tab), number=100, globals=globals())
        liste_y3.append(time3)
    
    # Tracer la courbe
    fig, ax = plt.subplots()

    ax.plot(liste_x, liste_y1, color="red", label="Tri par fusion")
    ax.plot(liste_x, liste_y2, color="blue", label="Tri par insertion")
    ax.plot(liste_x, liste_y3, color="green", label="Tri par sélection")
    
    ax.legend(loc="best")
    ax.set(xlabel="n (taille de la liste)", ylabel="Temps (s)", title="Illustration de la complexité")
    ax.grid()
    plt.show()

tracer_courbe(400)
