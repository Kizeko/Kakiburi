import os

from font_util import generate_image

# Character to generate
character = 0x3050

for root, dirs, files in os.walk("./fonts-test"):
        for file in files:
            if file.endswith(".ttf") or file.endswith(".otf"):
                    generate_image(character, root + "/" + file, "./images-test", "./images-test/{}_{}.png".format(hex(0x3042)[2:], file.split(".")[0]))