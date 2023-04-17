def pizza_a(n: int):
    if n == 0: # Cas de base
        return 0.2
    else: # Cas général
        return 0.5 * pizza_a(n-1) + 0.15 * pizza_b(n-1) + 0.15 * pizza_c(n-1)

def pizza_b(n: int):
    if n == 0: # Cas de base
        return 0.3
    else: # Cas général
        return 0.25 * pizza_a(n-1) + 0.4 * pizza_b(n-1) + 0.1 * pizza_c(n-1)

def pizza_c(n: int):
    if n == 0: # Cas de base
        return 0.5
    else: # Cas général
        return 0.25 * pizza_a(n-1) + 0.45 * pizza_b(n-1) + 0.75 * pizza_c(n-1)

def affichage(n: int):
    print(f"{'n':<4} │ {'a(n)':^8} │ {'b(n)':^8} │ {'c(n)':^8}")
    print("─────┼──────────┼──────────┼──────────")
    for i in range(n+1):
        print(f"{i:<4d} │ {pizza_a(i):^8.2%} │ {pizza_b(i):^8.2%} │ {pizza_c(i):^8.2%}")

def main():
    affichage(10)

if __name__ == "__main__":
    main()
