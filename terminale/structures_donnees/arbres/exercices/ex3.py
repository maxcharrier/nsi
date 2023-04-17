from arbre import Arbre

A2 = Arbre("F",
	gauche=Arbre("B",
		gauche=Arbre("A"),
		droite=Arbre("D",
			gauche=Arbre("C"),
			droite=Arbre("E")
		)
	),
	droite=Arbre("G",
		gauche=Arbre().arbre_vide,
		droite=Arbre("I",
			gauche=Arbre("H")
		)
	)
)

print(A2)

def parcours_infixe(arbre: Arbre):
	if arbre is not Arbre.arbre_vide:
		parcours_infixe(arbre.gauche())
		print(arbre.etiquette())
		parcours_infixe(arbre.droite())

parcours_infixe(A2)
