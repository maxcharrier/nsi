import matplotlib.pyplot as plt
from PIL import Image
from timeit import timeit


def rotation_iterative(img):
    (width, height) = img.size
    assert width == height, "L'image n'est pas carré !"

    tmp = Image.new("RGB",(width, width))
    for x in range(width):
        for y in range(width):
            # Tourner vers la droite
            (r,v,b) = img.getpixel((x, y))
            tmp.putpixel((width - 1 - y, x), (r, v, b))
            
            # Tourner vers la gauche
            #(r,v,b) = img.getpixel((x, y))
            #tmp.putpixel((y, width - 1 - x), (r, v, b))
    return tmp


def echanger_pixels(img, x0, y0, x1, y1):
    p0 = img.getpixel((x0, y0))
    p1 = img.getpixel((x1, y1))
    img.putpixel((x0, y0), p1)
    img.putpixel((x1, y1), p0)


def echanger_quadrants(img, x0, y0, x1, y1, n):
    for i in range(n):
        for j in range(n):
            echanger_pixels(img, x0 + i, y0 + j , x1 + i, y1 + j)


def tourner_quadrants(img, x0, y0, n):
    if n >= 2 :
        m = n // 2
        tourner_quadrants(img, x0, y0, m)
        tourner_quadrants(img, x0, y0 + m, m)
        tourner_quadrants(img, x0 + m, y0, m)
        tourner_quadrants(img, x0 + m, y0 + m, m)
        echanger_quadrants(img, x0, y0, x0 + m, y0, m)
        echanger_quadrants(img, x0, y0, x0 + m, y0 + m, m)
        echanger_quadrants(img, x0, y0, x0, y0 + m, m)


def rotation_recursive(img):
    (width, height) = img.size
    assert width == height, "L'image n'est pas un carré !"
    
    tourner_quadrants(img, 0, 0, width)


img = Image.open("diviser_pour_regner/exercices/ex4/pomme_512.jpeg")
#img.show()

#img1 = rotation_iterative(img)
#img1.show()

#rotation_recursive(img)
#img.show()


def tracer_courbe(n_max = 10):
    liste_x = []
    liste_y1 = []
    liste_y2 = []

    for n in range(n_max):
        # Tableau des abscisses
        liste_x.append(n)
        print(liste_x)

        # Tableau des ordonnées
        time1 = timeit(lambda: rotation_iterative(img), number=2, globals=globals())
        liste_y1.append(time1)
        print(liste_y1)

        time2 = timeit(lambda: rotation_recursive(img), number=2, globals=globals())
        liste_y2.append(time2)
        print(liste_y2)
    
    # Tracer la courbe
    fig, ax = plt.subplots()

    ax.plot(liste_x, liste_y1, color="red", label="Rotation itérative")
    ax.plot(liste_x, liste_y2, color="blue", label="Rotation récursive")
    
    ax.legend(loc="best")
    ax.set(xlabel="n (moyenne)", ylabel="Temps (s)", title="Illustration de la complexité")
    ax.grid()
    plt.show()


tracer_courbe()
