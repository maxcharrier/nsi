from pile import Pile

# Q1
p1 = Pile()
p1.push(10)
p1.push(20)
p1.push(30)
p1.push(40)

# Q2
"""
print(
	p1.pile.valeur,
	p1.pile.suivante.valeur,
	p1.pile.suivante.suivante.valeur,
	p1.pile.suivante.suivante.suivante.valeur
)
"""

# Q3
p1.afficher()

# Q4/Q5
print(p1.taille())

# Q6
p1.inserer(50, 2)
p1.afficher()
