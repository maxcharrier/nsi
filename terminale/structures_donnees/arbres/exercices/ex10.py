from arbre import Arbre

A2 = Arbre(1,
	gauche=Arbre(2,
		gauche=Arbre(4,
			gauche=Arbre(8),
			droite=Arbre(9)
		),
		droite=Arbre(5,
			gauche=Arbre(10)
		)
	),
	droite=Arbre(3,
		gauche=Arbre(6),
		droite=Arbre(7)
	)
)

print(A2)

def hauteur(arbre: Arbre):
	if arbre is Arbre.arbre_vide:
		return -1
	else:
		return 1 + max(hauteur(arbre.gauche()), hauteur(arbre.droite()))

print(hauteur(A2))
