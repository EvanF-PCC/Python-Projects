from PIL import ImageSequence, Image, GifImagePlugin
import random

# made this coz i was bored
# made by EvanF

fd = input("Input the name of a valid .gif file, including the extension.\n>>>")
img = None
try:
    img = Image.open("pillow_imagedraw.gif")
except FileNotFoundError:
    print("The file couldn't be found.")
    exit()

if ImageSequence.Iterator(img)[0].n_frames > 50:
    print("Warning! this gif is longer than 50 frames, and will take forever on a bad computer. Proceed? (Y/N)")
    if input(">>").lower() == "y":
        pass
    else:
        exit()
print(img)

fin = []

bw = False

if len(ImageSequence.Iterator(img)[0].split()) == 1:
    bw = True
else:
    bw = False

for frame in ImageSequence.Iterator(img):
    if not bw:
        try:
            r, g, b = frame.split()
        except ValueError:
            r, g, b, a = frame.split()

    else:

        r, g, b = Image.new("RGB", frame.size).split()

    for y_position in range(frame.height):
        for x_position in range(frame.width):
            if bw:
                BW_val = int(frame.getpixel((x_position, y_position)))
                rv = int(BW_val * random.uniform(0.001, 5) * 0.5)
                gv = int(BW_val * random.uniform(0.001, 2) * 0.5)
                bv = int(BW_val * random.uniform(0.000001, 1) * 0.5)
            else:

                rv = int(r.getpixel((x_position, y_position)) * random.uniform(0.001, 5) * 0.5)
                gv = int(g.getpixel((x_position, y_position)) * random.uniform(0.001, 2) * 0.5)
                bv = int(b.getpixel((x_position, y_position)) * random.uniform(0.000001, 1) * 0.5)

            r.putpixel((x_position, y_position), rv)
            g.putpixel((x_position, y_position), gv)
            b.putpixel((x_position, y_position), bv)
    j = Image.merge("RGB", (r, g, b))

    fin.append(j)
    print("Finished frame " + str(len(fin)))

o = input("Input a name for the file, without the '.gif' part")
fin[0].save(o + ".gif", save_all=True, append_images=fin[1:], optimize=False, duration=ImageSequence.Iterator(img)[0].info['duration'], loop=0)
print("Program finished.")
