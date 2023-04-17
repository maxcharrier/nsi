from math import pi

def aire_carre(x: float):
    """
    Calculer l'aire d'un carré
    x : longueur d'un côté
    retour : aire du carré
    """
    return x * x

def aire_triangle(b: float, h: float):
    """
    Calculer l'aire d'un triangle
    b : base
    h : hauteur
    retour : aire du triangle
    """
    return (b * h) / 2

def aire_trapeze(B: float, b: float, h: float):
    """
    Calculer l'aire d'un trapèze
    B : grande base
    b : petite base
    h : hauteur
    retour : aire du trapèze
    """
    return (B + b) * h / 2

def aire_disque(r: float):
    """
    Calculer l'aire d'un disque
    r : rayon
    retour : aire du disque
    """
    return pi * 2 * r

print("Module pour calculer des aires chargées")

if __name__ == "__main__":
    print("Je suis un module")
