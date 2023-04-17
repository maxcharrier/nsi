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

tab = [6, 42, 69, 24, 78, 1, 4]
tri_insertion(tab)
print(tab)
