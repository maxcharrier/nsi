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

def parcours_min_max(arbre: Arbre):
	if arbre is not Arbre.arbre_vide:
		if arbre.gauche() is Arbre.arbre_vide and arbre.droite() is Arbre.arbre_vide:
			return arbre.etiquette(), arbre.etiquette()
		
		elif arbre.gauche() is Arbre.arbre_vide:
			_, droite = parcours_min_max(arbre.droite())
			etiquette_min = min(arbre.etiquette(), droite)
			etiquette_max = max(arbre.etiquette(), droite)
		
		elif arbre.droite() is Arbre.arbre_vide:
			gauche, _ = parcours_min_max(arbre.gauche())
			etiquette_min = min(arbre.etiquette(), gauche)
			etiquette_max = max(arbre.etiquette(), gauche)
		
		else:
			min_gauche, max_gauche = parcours_min_max(arbre.gauche())
			min_droite, max_droite = parcours_min_max(arbre.droite())
			etiquette_min = min(arbre.etiquette(), min_gauche, min_droite)
			etiquette_max = max(arbre.etiquette(), max_gauche, max_droite)
		
		return etiquette_min, etiquette_max

print(parcours_min_max(A2))
