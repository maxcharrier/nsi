def sissa(n: int) -> int:
    assert type(n) == int, "n doit être un entier naturel"
    assert n >= 0, "n doit être un entier naturel"
    assert n < 64, "n doit être inférieur à 64"

    if n == 0: # Cas de base
        return 1
    else: # Cas général
        return sissa(n-1) + 2**n

def sissa2(n: int) -> int:
    assert type(n) == int, "n doit être un entier naturel"
    assert n >= 0, "n doit être un entier naturel"
    assert n < 64, "n doit être inférieur à 64"

    if n == 0: # Cas de base
        return 1, 1 # U(0), S(0)
    else: # Cas général
        un = 2 * sissa2(n-1)[0]
        sn = 2**n + sissa2(n-1)[1]
        return un, sn # 2 * U(n-1), 2^n + S(n-1)

def main():
    r = sissa(4)
    print(r)
    #print([sissa(e) for e in range(64)][-1])

    r2 = sissa2(4)
    print(r2)

if __name__ == "__main__":
    main()
