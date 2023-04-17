from arbre import Arbre

A1 = Arbre(13,
	gauche=Arbre(8,
		gauche=Arbre(1,
			droite=Arbre(6)
		),
		droite=Arbre(11)
	),
	droite=Arbre(17,
		gauche=Arbre(15),
		droite=Arbre(25,
			gauche=Arbre(22),
			droite=Arbre(27)
		)
	)
)

A2 = Arbre(30,
	gauche=Arbre(25,
		gauche=Arbre(18,
			gauche=Arbre(9)
		),
		droite=Arbre(29,
			gauche=Arbre(26,
				droite=Arbre(28)
			)
		)
	),
	droite=Arbre(41,
		droite=Arbre(52,
			gauche=Arbre(48),
			droite=Arbre(60)
		)
	)
)

def est_abr(arbre: Arbre):
	if arbre is not Arbre.arbre_vide:
		if arbre.gauche() is Arbre.arbre_vide and arbre.droite() is Arbre.arbre_vide:
			return True
		
		if arbre.gauche() is Arbre.arbre_vide:
			gauche_abr = True
		elif arbre.gauche().etiquette() <= arbre.etiquette() and est_abr(arbre.gauche()):
			gauche_abr = True
		else:
			gauche_abr = False
		
		if arbre.droite() is Arbre.arbre_vide:
			droite_abr = True
		elif arbre.droite().etiquette() > arbre.etiquette() and est_abr(arbre.droite()):
			droite_abr = True
		else:
			droite_abr = False
		
		return gauche_abr and droite_abr
	
	else:
		return False

print(est_abr(A1))
print(est_abr(A2))

def verifier_val(arbre: Arbre, val: int):
	if arbre.etiquette() == val:
		return True
	elif val < arbre.etiquette() and arbre.gauche() is not Arbre.arbre_vide:
		return verifier_val(arbre.gauche(), val)
	elif val > arbre.etiquette() and arbre.droite() is not Arbre.arbre_vide:
		return verifier_val(arbre.droite(), val)
	else:
		return False

print(verifier_val(A1, 22))
