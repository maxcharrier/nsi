import turtle as t

def arbre(n: int, longueur: float) -> float:
    if n < 0: # Cas de base
        return longueur
    else: # Cas général
        t.forward(longueur)
        t.left(30)
        l1 = arbre(n - 1, longueur * 0.6)
        t.right(60)
        l2 = arbre(n - 1, longueur * 0.6)
        t.left(30)
        t.forward(-longueur)

        return longueur + l1 + l2

def arbre2(longueur: float):
    if longueur < 3: # Cas de base
        return longueur
    else: # Cas général
        t.forward(longueur)
        t.left(45)
        arbre2(longueur * 0.6)
        t.right(90)
        arbre2(longueur * 0.6)
        t.left(45)
        t.forward(-longueur)

def main():
    t.hideturtle()
    t.speed(10)
    t.up()
    t.goto(-100, 0)
    #t.setheading(90)
    t.down()

    r = arbre(2, 100)
    print(r)

    #arbre2(020)
    
    t.done()

if __name__ == "__main__":
    main()