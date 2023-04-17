from PIL import Image

def image_gris(img):
    (width, height) = img.size
    tmp = Image.new("RGB", (width, height))
    
    for x in range(width):
        for y in range(height):
            (r,v,b) = img.getpixel((x,y))
            niveau_gris = round(0.299 * r + 0.587 * v + 0.114 * b)
            tmp.putpixel((x,y), (niveau_gris, niveau_gris, niveau_gris))
    
    return tmp


def inverser_rouge_bleu(img):
    (width, height) = img.size
    tmp = Image.new("RGB", (width, height))

    for x in range(width):
        for y in range(height):
            (r,v,b) = img.getpixel((x, y))
            r,v,b = b,v,r
            tmp.putpixel((x, y), (r, v, b))
    
    return tmp


def inverser_horizontal(img):
    (width, height) = img.size
    tmp = Image.new("RGB", (width, height))

    for x in range(width):
        for y in range(height):
            (r,v,b) = img.getpixel((x, y))
            x_i = width - 1 - x  # Inverser l'abscisse
            tmp.putpixel((x_i, y) , (r, v, b))
    
    return tmp


def fusionner_images(img1, img2):
    (width1, height1) = img1.size
    (width2, height2) = img2.size
    tmp = Image.new("RGB", (width1, height1))
    
    for x in range(width1):
        for y in range(height1):
            if x < width2 and y < height2:
                (r,v,b,_) = img2.getpixel((x, y))
                if 0 <= r < 127 and 128 < v <= 255 and 0 <= b < 127:
                    (r,v,b) = img1.getpixel((x,y))
            else:
                (r,v,b) = img1.getpixel((x, y))
                
            tmp.putpixel((x, y), (r, v, b))
    
    return tmp


def main():
    img = Image.open("images/image1.png")
    vaisseau = Image.open("images/vaisseau_spatial_300_200.png")
    
    """
    img1 = image_gris(img)
    img1.show()
    img2 = inverser_rouge_bleu(img)
    img2.show()
    img3 = inverser_horizontal(img)
    img3.show()
    """

    img4 = fusionner_images(img, vaisseau)
    img4.show()


if __name__ == "__main__":
    main()
