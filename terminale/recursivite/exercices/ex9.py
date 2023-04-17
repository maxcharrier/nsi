import turtle as t

def koch(n: int, longueur=200):
    if n == 0: # Cas de base
        t.forward(longueur)
    else: # Cas général
        koch(n - 1, longueur / 3)
        t.left(60)
        koch(n - 1, longueur / 3)
        t.right(120)
        koch(n - 1, longueur / 3)
        t.left(60)
        koch(n - 1, longueur / 3)

def flocon(n: int):
	for _ in range(3) :
		koch(n)
		t.left(-120)

def main():
    t.hideturtle()
    t.speed(10)
    t.up()
    t.goto(-200, 50)
    t.down()

    koch(2)

    t.up()
    t.forward(20)
    t.down()

    flocon(2)

    t.done()

if __name__ == "__main__":
    main()
