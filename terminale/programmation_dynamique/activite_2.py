a = 10
tab1 = [1, 2, 3, 4, 5]
tab2 = tab1

def fonction1(a):
    a += 1
    return a


def fonction2():
    global a
    a += 1
    return a


def fonction3(tab):
    tab[4] = 6
    return tab


def fonction4():
    tab1[4] = 6
    return tab1


def fonction5():
    a += 1
    return a


print(fonction1(a))
print(a)

print(fonction2())
print(a)

print(fonction3(tab1))
print(tab1)

tab3 = fonction3(tab1)
print(id(tab1))
print(id(tab2))
print(id(tab3))
