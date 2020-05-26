import random

from PIL import Image

try:
    img = Image.open(input("Input a .png file name: "))
except FileNotFoundError:
    exit("File not found.")
turns = int(input("How many times?: "))
try:
    r1, g1, b1, a1 = img.split()
except ValueError:
    r1, g1, b1 = img.split()
for i in range(turns):

    for y in range(img.height):
        for x in range(img.width):
            rv = int(r1.getpixel((x, y)) * random.uniform(0.001, 5) * 0.5)
            gv = int(g1.getpixel((x, y)) * random.uniform(0.001, 2) * 0.5)
            bv = int(b1.getpixel((x, y)) * random.uniform(0.000001, 1) * 0.5)

            r1.putpixel((x, y), rv)
            g1.putpixel((x, y), gv)
            b1.putpixel((x, y), bv)
    print("Iteration " + str(i + 1) + " Finished.")
img = Image.merge("RGB", (r1, g1, b1))

img.save("deepfried.png")
print("Saved as deepfried.png")
