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

def parcours_infixe(arbre: Arbre):
	if arbre is not Arbre.arbre_vide:
		parcours_infixe(arbre.gauche())

		if arbre.etiquette() % 2 == 0:
			print(f"{arbre.etiquette()} est pair")
		else:
			print(f"{arbre.etiquette()} est impair")
		
		parcours_infixe(arbre.droite())

parcours_infixe(A2)
