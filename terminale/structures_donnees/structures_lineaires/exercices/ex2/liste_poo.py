from classe_liste import *

l1 = Cellule(10, Cellule(20, Cellule(30, Cellule(40))))
print(
    l1.valeur,
    l1.suivante.valeur,
    l1.suivante.suivante.valeur,
    l1.suivante.suivante.suivante.valeur
)

l2 = Liste()
l2.ajouter(40)
l2.ajouter(30)
l2.ajouter(20)
l2.ajouter(10)
print(
    l2.tete.valeur,
    l2.tete.suivante.valeur,
    l2.tete.suivante.suivante.valeur,
    l2.tete.suivante.suivante.suivante.valeur
)
print(l2.afficher())
print(l2.taille())

l2.inserer(50, 2)
print(l2.afficher())
print(l2.long)
