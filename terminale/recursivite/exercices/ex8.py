import turtle as t

def spirale(n: int, longueur=5) -> int:
    if n == 0: # Cas de base
        return
    else: # Cas général
        t.forward(longueur)
        t.left(90)
        s = longueur + spirale(n - 1, longueur + 5)
        return s

def main():
    t.hideturtle()
    t.speed(10)

    l = spirale(50)
    print(l)

    t.done()

if __name__ == "__main__":
    main()
