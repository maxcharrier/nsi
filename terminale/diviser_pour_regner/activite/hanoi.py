def hanoi(n, debut, fin, aux):
    if n == 1: # cas de base
        print(f"Disque {n} : {debut} -> {fin}")
    else: # diviser pour regner
        hanoi(n-1, debut, aux, fin)
        print(f"Disque {n} : {debut} -> {fin}")
        hanoi(n-1, aux, fin, debut)

hanoi(3, "A", "C", "B")
