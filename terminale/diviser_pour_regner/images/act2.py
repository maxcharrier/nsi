from PIL import Image

img = Image.open("images/image1.png")
#img.putpixel((0, 0), (255, 255, 255))
#img.show()
#img.save("images/image2.png")

def ligne_bleu(n: int):
    (L,H) = img.size
    c = 0

    """
    while n != H-1 and c != L-1:
        img.putpixel((c, n), (0, 0, 255))
        c += 1
    """

    for c in range(L):
        img.putpixel((c, n),  (0, 0, 255))

ligne_bleu(18)

img.show()
img.save("images/image2.png")
