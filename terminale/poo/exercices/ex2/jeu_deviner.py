import joueurs


def main():
    #joueur1 = joueurs.JoueurChoix("Paul", 10)
    #joueur1.choisir_nombre()
    #print(joueur1.verifier_proposition(6))

    #joueur2 = joueurs.JoueurDeviner("Julie", 10)
    #print(joueur2.proposer_nombre())

    jeu = joueurs.JeuDeviner("Coco", "Lulu", 10)
    jeu.lancer_jeu()


if __name__ == "__main__":
    main()
