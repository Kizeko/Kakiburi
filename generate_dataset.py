import numpy as np
import cv2
import pandas as pd
from fontTools.ttLib import TTFont
from tqdm.auto import tqdm

from csvscript import *
from font_util import *

infos = pd.read_csv("./fonts.csv", index_col=0)
infos.head()

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
