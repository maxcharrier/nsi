import tkinter as tk
import tkinter.messagebox
from tkinter.constants import CENTER, TOP
import puces


# ================
# PARTIE LOGIQUE
# =================

# GESTION DES PUCES ET DE LA COURSE

# instanciation des puces
dolly = puces.Puce("Dolly", "blue", 0)
billou = puces.Puce("Billou", "red", 0)
zitron = puces.Puce("Zitron", "yellow", 0)
max = puces.Puce("Max", "orange", 0)
marc = puces.Puce("Marc", "black", 0)
nico = puces.Puce("Nicolas", "green", 0)

# nombre de cases à traverser pour gagner la course
cases_max = 20 # ne pas hésiter à changer cette variable

# instanciation de la course et ajout des puces
course = puces.Course(cases_max)

# ajouts des puces à la course
course.ajouter_puce(dolly)
course.ajouter_puce(billou)
course.ajouter_puce(zitron)
course.ajouter_puce(max)
course.ajouter_puce(marc)
course.ajouter_puce(nico)


# =================
# PARTIE GRAPHIQUE ( on y touche pas :] )
# =================

# CONSTANTE GLOBALE
NB_JOUEURS = len(course.get_puces())
NB_CASES = cases_max + NB_JOUEURS


# GESTION DE LA FENETRE

# dimensions de la fenete
hauteur, largeur = 500, 500

# creation de la fenetre avec titre et dimensions
fenetre = tk.Tk() 
fenetre.title("Jeu de Puce")
fenetre.geometry(f"{largeur}x{hauteur + 20}")


# GESTION DU GAGNANT

# ajout de la zone de texte pour afficher le gagnant
gagnant = tk.Label(fenetre, text="", height=2, width=50, background="white")
gagnant.config(anchor=CENTER)
gagnant.pack()


# GESTION DU PLATEAU ET DES CASES

# création du plateau de la course
plateau = tk.Canvas(fenetre, width=largeur, height=hauteur / NB_CASES * NB_JOUEURS, background="white")
plateau.pack(side=TOP)

case_hauteur = hauteur / NB_CASES
case_largeur = largeur / NB_CASES

# création des grilles
def creer_cadrillage(nb_joueurs: int):
    taille = 500 / NB_CASES
    grille_x = 0
    while grille_x <= nb_joueurs:
        plateau.create_line(0, taille * grille_x, largeur, taille * grille_x, fill="#DCDCDC")
        grille_x += 1

    grille_y = 0
    while grille_y <= NB_CASES:
        if grille_y == cases_max:
            return
            
        plateau.create_line(taille * grille_y, 0, taille * grille_y, case_hauteur * nb_joueurs, fill="#DCDCDC")
        grille_y += 1

# fonction pour remplir une case
def remplir_case(x: int, y: int, color: str):
    x0 = x * case_largeur
    y0 = y * case_hauteur
    x1 = x0 + case_largeur
    y1 = y0 + case_hauteur
    plateau.create_rectangle(x0, y0, x1, y1, fill=color, outline=color)


# GESTION DU CLAVIER

# faire avancer les puces
def avancer(event):
    puces = course.deplacer_puces()
    
    for puce in puces:
        # verification pour gagner la course
        if puce[1] >= cases_max:
            remplir_case(puce[1], puces.index(puce), puce[0].get_couleur())

            fenetre.unbind("<space>")

            if puce[1] >= 10:
                gagnant.config(text=f"{puce[0].get_nom()} est arrivé 1er")

        # sinon les puces continue à avancer :)
        remplir_case(puce[1], puces.index(puce), puce[0].get_couleur())

# appuyer sur ESPACE pour faire avancer
fenetre.bind("<space>", avancer)


# BOUCLE PRINCIPALE
def main():
    # màj fenetre + event clavier
    fenetre.update()
    fenetre.update_idletasks()

    # ajout des grilles
    creer_cadrillage(NB_JOUEURS)
    
    # case de depart
    for i in range(len(course.get_puces())):
        remplir_case(0, i, course.get_puces()[i].get_couleur())
    
    # pop-up message info
    tk.messagebox.showinfo("Jeu de Puce", "Appuyer sur ESPACE pour commencer la course !")

if __name__ == "__main__":
    # reset
    plateau.delete("all")
    
    # lancement
    fenetre.after(0, main())
    fenetre.mainloop()
