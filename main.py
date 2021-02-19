from PIL import Image
from math import sqrt

image = Image.open("Image.jpg")
pixels = image.load()
size_w, size_h = image.size

colors = []
for h in range(size_h):
    for w in range(size_w):
        try:
            r, g, b = image.getpixel((h, w))
        except:
            pass
        brightness = sum([r, b, g]) // 3
        colors.append((r, g, b, brightness))

def make_image():
    global colors
    color_index = len(colors)
    colors = sorted(colors, key=lambda x: (x[3], x[0], x[1], x[2]))
    for h in range(size_h):
        for w in range(size_w):
            pixels[w, h] = colors[color_index-1]
            color_index -= 1
    image.save("Test.jpg")

make_image()
