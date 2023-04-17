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

def nb_feuilles(arbre: Arbre):
	if arbre is not Arbre.arbre_vide:
		if arbre.gauche() is Arbre.arbre_vide and arbre.droite() is Arbre.arbre_vide:
			return 1
		else:
			return nb_feuilles(arbre.gauche()) + nb_feuilles(arbre.droite())
	else:
		return 0

r = nb_feuilles(A2)
print(f"Il y a {r} feuilles")
