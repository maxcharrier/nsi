def p(n):
    if n == 1:
        return n
    else:
        return p(n-1) * n

print(p(3))