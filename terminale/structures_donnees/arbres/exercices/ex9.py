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

def taille(arbre: Arbre):
	if arbre is Arbre.arbre_vide:
		return 0
	else:
		return 1 + taille(arbre.gauche()) + taille(arbre.droite())

print(taille(A2))
