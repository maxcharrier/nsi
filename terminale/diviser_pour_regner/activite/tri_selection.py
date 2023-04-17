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

tab = [6, 42, 69, 24, 78, 1, 4]
tri_selection(tab)
print(tab)
