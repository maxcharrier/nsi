from arbre_listes import *

A1 = noeud(1,
	noeud(2,
		noeud(4,
			noeud(8, arbre_vide(), arbre_vide()),
			noeud(9, arbre_vide(), arbre_vide())
		),
		noeud(5,
			noeud(10, arbre_vide(), arbre_vide()),
			arbre_vide()
		)
	),
	noeud(3,
		noeud(6, arbre_vide(), arbre_vide()),
		noeud(7, arbre_vide(), arbre_vide())
	)
)

A2 = noeud("F",
	noeud("B",
		noeud("A", arbre_vide(), arbre_vide()),
		noeud("D",
			noeud("C", arbre_vide(), arbre_vide()),
			noeud("E", arbre_vide(), arbre_vide())
		)
	),
	noeud("G",
		arbre_vide(),
		noeud("I",
			noeud("H", arbre_vide(), arbre_vide()),
			arbre_vide()
		)
	)
)

print(A1)
print(A2)
