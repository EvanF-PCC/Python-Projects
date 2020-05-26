from PIL import Image

img = Image.open("pencils.png")

(r, g, b, a) = img.split()

for y in range(img.height):
    for x in range(img.width):
        Rp: int = r.getpixel((x, y))
        Gp: int = g.getpixel((x, y))
        Bp: int = b.getpixel((x, y))
        A: int= a.getpixel((x, y))
        avg: int = (Rp + Gp + Bp + A) // 4
        # r.putpixel((x, y), avg)
        # g.putpixel((x, y), avg)
        # b.putpixel((x, y), avg)
        img.putpixel((x, y), (avg, avg, avg, avg))

#img2 = Image.merge("RGBA", (r,g,b,a))
img.save("pencils3.png")
