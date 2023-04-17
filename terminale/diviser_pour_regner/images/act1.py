from PIL import Image

img = Image.open("images/image1.png")
img.show()

(r,v,b) = img.getpixel((5, 10))
print(f"canal rouge : {r}, canal vert : {v}, canal bleu : {b}")

(L,H) = img.size
print(f"La largeur de l'image est : {L}, la hauteur de l'image est {H}")

(r,v,b) = img.getpixel((L-1, 0))
print(f"canal rouge : {r}, canal vert : {v}, canal bleu : {b}")

(r,v,b) = img.getpixel((L-1, H-1))
print(f"canal rouge : {r}, canal vert : {v}, canal bleu : {b}")

(r,v,b) = img.getpixel((0, H-1))
print(f"canal rouge : {r}, canal vert : {v}, canal bleu : {b}")
