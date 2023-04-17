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

def parcours_largeur(arbre: Arbre):
	if arbre is not Arbre.arbre_vide:
		file = []
		file.insert(0, arbre)

		while file != []:
			noeud: Arbre = file.pop()
			print(noeud.etiquette())

			if noeud.gauche() is not Arbre.arbre_vide:
				file.insert(0, noeud.gauche())
			if noeud.droite() is not Arbre.arbre_vide:
				file.insert(0, noeud.droite())


parcours_largeur(A2)
