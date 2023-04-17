import geometrie as aires

def main():
    aire_carre = aires.aire_carre(5)
    print(aire_carre)

    aire_triangle = aires.aire_triangle(2, 5)
    print(aire_triangle)

    aire_totale = aires.aire_carre(10) + aires.aire_triangle(10, 10)
    print(aire_totale)

    aire_trapeze = aires.aire_trapeze(10, 8, 5)
    print(aire_trapeze)

    aire_disque = aires.aire_disque(2.5)
    print(aire_disque)

if __name__ == "__main__":
    main()
