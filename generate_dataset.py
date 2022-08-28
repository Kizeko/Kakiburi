from PIL import Image, ImageFont, ImageDraw
import os
import numpy as np
import cv2
import pandas as pd
from fontTools.ttLib import TTFont
from tqdm.auto import tqdm

import csvscript

width, height = 60, 60

def generate_image(character, font_path, image_path):
    background_color = 'black'
    text_color = (255)
    color_mode = 'L'
    font_size=55


    font = ImageFont.truetype(font=font_path, size=font_size)
    image = Image.new(mode=color_mode, size=(width, height), color=background_color)
    image_draw = ImageDraw.Draw(image)

    bbox = image_draw.textbbox((0, 0), text=chr(character), font=font)
    xy = ((width - (bbox[2] + bbox[0])) / 2, (height - (bbox[3] + bbox[1])) / 2)

    image_draw.text(xy=xy, text=chr(character), fill=text_color, font=font)

    for i in range(width):
        for j in range(height):
            if image.getpixel((i, j)) != 0:
                if not os.path.exists("./images/U+{}".format(hex(character)[2:])):
                    os.mkdir(os.path.dirname(image_path))
                image.save(image_path)
                return True
    
    return False

unicodes = [0x3000,
            0x303f,
            0x3041,
            0x309f,
            0x30a0,
            0x30ff,
            0xff00,
            0xffef,
            0x4e00,
            0x9faf]

total_unicodes = 0
for i in range(len(unicodes), 0, -2):
    total_unicodes += unicodes[i - 1] - unicodes[i - 2]

infos = pd.read_csv("./fonts.csv", index_col=0)
infos.head()

def char_in_font(unicode_char, font):
    for cmap in font['cmap'].tables:
        if cmap.isUnicode():
            if ord(unicode_char) in cmap.cmap:
                return True
    return False

dataset_x = []
dataset_y = []

for index, info in infos.iterrows():
    i = 0
    while i < len(unicodes) - 1:
        start = unicodes[i]
        end = unicodes[i + 1]
        print("part (U+{})-(U+{}) of the font {} :".format(hex(start)[2:], hex(end)[2:], info['name']))
        for j in tqdm(range(start, end)):
            font = TTFont(info['path'])
            if not char_in_font(chr(j), font):
                continue

            img_path = "./images/U+{}/{}.png".format(hex(j)[2:], index)

            valid = generate_image(j, info['path'], img_path)
            if not valid:
                continue

            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            dataset_x.append(img)
            dataset_y.append(j)
        i += 2

np.save("./dataset_x.npy", np.array(dataset_x).reshape(-1, width, height, 1))
np.save("./dataset_y.npy", np.array(dataset_y).reshape(-1, 1))
