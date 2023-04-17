def liste_vide():
    return []

def cellule(etiquette, liste):
    return [etiquette, liste]

def valeur(liste: list):
    return liste[0]

def suite(liste: list):
    return liste[1]

def est_vide(liste: list) -> bool:
    return liste == liste_vide()


l1 = cellule(10, cellule(20, cellule(30, cellule(40, liste_vide()))))
print(l1)

def inverser(liste: list):
    if est_vide(liste):
        return liste_vide()
    
    copie = liste_vide()
    while not est_vide(liste):
        copie = cellule(valeur(liste), copie)
        liste = suite(liste)
    
    return copie

l1_retourner = inverser(l1)
print(l1_retourner)

def taille(liste: list):
    long = 0
    if est_vide(liste):
        return long

    while not est_vide(liste):
        liste = suite(liste)
        long += 1
    
    return long

taille_l1 = taille(l1)
print(taille_l1)

def borne(liste: list):
    if est_vide(liste):
        return (liste_vide(), liste_vide())
    
    a = valeur(liste)
    while not est_vide(suite(liste)):
        liste = suite(liste)
    b = valeur(liste)

    return a, b

borne_l1 = borne(l1)
print(borne_l1)
