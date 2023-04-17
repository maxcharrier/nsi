from structures_donnees.exercices.ex7.pile import *

# Q2
p1 = pile_vide()
p1 = push(40, p1)
p1 = push(30, p1)
p1 = push(20, p1)
p1 = push(10, p1)
print(p1)

# enlever de la pile
(valeur, p1) = pop(p1)
print(valeur, p1)

# sommet de la pile
print(sommet(p1))

# afficher la pile
print("\nafficher la pile")
afficher(p1)
print()

# Q3
print("\ninverse la pille")
p2 = inverser(p1)
print(p2)

# Q4
print("\ntaille de la pile")
print(taille(p1))
print(taille(p2))

# Q5
print("\nborne de la pille")
print(borne(p1))
print(borne(p2))
