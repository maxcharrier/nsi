from arbre import Arbre

A1 = Arbre("F",
	gauche=Arbre("B",
		gauche=Arbre("A"),
		droite=Arbre("D",
			gauche=Arbre("C"),
			droite=Arbre("E")
		)
	),
	droite=Arbre("G",
		droite=Arbre("I",
			gauche=Arbre("H")
		)
	)
)

def verifier_val(arbre: Arbre, val):
	if arbre is not Arbre.arbre_vide:
		if arbre.etiquette() == val:
			return True
		elif verifier_val(arbre.gauche(), val):
			return True
		elif verifier_val(arbre.droite(), val):
			return True
		else:
			return False
	else:
		return False

print(verifier_val(A1, "B"))
