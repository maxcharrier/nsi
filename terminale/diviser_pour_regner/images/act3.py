from PIL import Image

img = Image.new("RGB", (300, 200))
#img.show()

def fond_blanc(img: Image):
    (L,H) = img.size

    for c in range(L):
        for l in range(H):
            img.putpixel((c, l), (255, 255, 255))

fond_blanc(img)
#img.show()

def f(x):
    (L,H) = img.size
    return (H-1)/(L-1) * x

print(f(100))

def tracer_courbe(a: int, b: int, c: tuple[int]):
    (L,H) = img.size
    assert b < L, "courbe plus grande que l'image !"

    for x in range(a, b+1):
        y = H - 1 - int(f(x))
        img.putpixel((x, y), c)

tracer_courbe(0, 299, (255, 0, 0))
img.show()
