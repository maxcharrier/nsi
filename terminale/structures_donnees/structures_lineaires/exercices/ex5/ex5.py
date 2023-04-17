from structures_donnees.exercices.ex5.file import *

# Q1
f1 = Cellule(10, Cellule(20, Cellule(30, Cellule(40))))
print(
	f1.valeur,
	f1.suivante.valeur,
	f1.suivante.suivante.valeur,
	f1.suivante.suivante.suivante.valeur
)

# Q2
print("────────────────")

f2 = File()
f2.push(10)
f2.push(20)
f2.push(30)
f2.push(40)
print(
	f2.tete.valeur,
	f2.tete.suivante.valeur,
	f2.tete.suivante.suivante.valeur,
	f2.queue.valeur
)

# Q3
print(f2.afficher())

# Q4
print(f2.taille())

# retirer element
print("────────────────")
elm = f2.pop()
print(elm)
print(f2.afficher())
print(f2.taille())
