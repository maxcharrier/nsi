from arbres.exercices.arbre import Arbre

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

def parcours_prefixe(arbre: Arbre):
	if arbre is not Arbre.arbre_vide:
		print(arbre.etiquette())
		parcours_prefixe(arbre.gauche())
		parcours_prefixe(arbre.droite())

parcours_prefixe(A2)
