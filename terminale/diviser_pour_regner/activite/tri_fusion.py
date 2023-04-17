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
    else: # diviser
        tab1 = tab[:n//2]
        tab2 = tab[n//2:]

        # regner
        tab1_trie = tri_fusion(tab1)
        tab2_trie = tri_fusion(tab2)

        # combiner
        resultat = fusion(tab1_trie, tab2_trie)
        
        return resultat

tab = [23, 12, 4, 56, 35, 32, 42, 57, 3]
r = tri_fusion(tab)
print(r)
