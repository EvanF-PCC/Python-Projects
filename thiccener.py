from PIL import Image

try:
    img = Image.open(input("Input the filename of a .png picture: "))
except FileNotFoundError:
    exit("File not found.")
scale = int(input("input the thiccening scale: "))

if img.width % scale != 0:
    exit("Invalid size")

img2 = Image.new("RGBA", (img.width * scale, img.height))
try:
    r1, g1, b1, a1 = img.split()
except ValueError:
    r1, g1, b1 = img.split()
try:
    r2, g2, b2, a2 = img2.split()
except ValueError:
    r2, g2, b2 = img2.split()

cols1 = [r1, g1, b1]
cols2 = [r2, g2, b2]

for y in range(img.height):
    for x in range(img.width):
        rv = r1.getpixel((x, y))
        gv = g1.getpixel((x, y))
        bv = b1.getpixel((x, y))

        for i in range(scale):
            r2.putpixel((scale * x + (i - 1), y), rv)
        for i in range(scale):
            g2.putpixel((scale * x + (i - 1), y), gv)
        for i in range(scale):
            b2.putpixel((scale * x + (i - 1), y), bv)

img2 = Image.merge("RGB", (r2, g2, b2))
img2.save("thicc.png")
print("Saved as thicc.png")
