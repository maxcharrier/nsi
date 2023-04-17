def fac(n: int) -> int:
    assert type(n) == int, "n doit être un entier naturel"
    assert n >= 0, "n doit être un entier naturel"

    if n == 0 or n == 1: # Cas de base
        print("n", "n!")
        print(n, 1)

        return 1
    else: # Cas général
        f = fac(n - 1) * n
        print(n, f)

        return f

def main():
    fac(4)

    # Tests
    assert fac(0) == 1
    assert fac(4) == 24
    assert fac(7) == 5040

if __name__ == "__main__":
    main()
