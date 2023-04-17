# 4.1
def file_vide():
    return []

def file(valeur, file):
    return [valeur, file]

def push(valeur, file):
    if est_vide(file):
        return [valeur, file_vide()]
    else:
        return [file[0], push(valeur, file[1])]

def pop(file):
    return (file[0], file[1])

def est_vide(file):
    return file == file_vide()

# 4.2
f1 = file_vide()
f1 = push(10, f1)
f1 = push(20, f1)
f1 = push(30, f1)
f1 = push(40, f1)

print(f1)

# 4.4
def taille(file):
    copie = file
    long = 0
    while not est_vide(copie):
        _, copie = pop(copie)
        long += 1

    return long

print(taille(f1))

# 4.5
def borne(file):
    if est_vide(file):
        return file_vide(), file_vide()

    copie = file
    a, copie = pop(copie)
    while not est_vide(copie):
        b, copie = pop(copie)

    return a, b

print(borne(f1))
