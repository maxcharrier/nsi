def fibo_mem(n, mem):
    tab = "\t" * (len(mem)-n-1)
    print(tab, n, mem, "Appel")

    # cas de base
    if n in (0, 1):
        mem[n] = n
        print(tab, n, mem, "Retour")
        return n

    # vérification : programmation dynamique
    if mem[n] != 0:
        return mem[n]

    # cas récursif
    mem[n] = fibo_mem(n-1, mem) + fibo_mem(n-2, mem)
    print(tab, n, mem, "Retour")
    return mem[n]


n = 4
mem = [0] * (n+1)
fibo_mem(n, mem)
