import numpy as np
import cv2
import pandas as pd
from tqdm.auto import tqdm

from csvscript import *
from font_util import *

# Import the generated csv file containing the fonts information
infos = pd.read_csv("./fonts.csv", index_col=0)

# Datasets
dataset_x = []
dataset_y = []

# Generate the dataset
for index, info in infos.iterrows():
    i = 0
    while i < len(unicodes) - 1:
        start = unicodes[i]
        end = unicodes[i + 1]
        print("\nStarted Generating the part (U+{})-(U+{}) of the font {} (#{}) :".format(hex(start)[2:], hex(end)[2:], info['name'], index))
        for j in tqdm(range(start, end)):
            # Path of the image directory that will be generated
            img_dir_path = "./images/U+{}".format(hex(j)[2:].capitalize())
            # Path of the image that will be generated
            img_path = img_dir_path + "/{}_{}.png".format(hex(j)[2:].capitalize(), index)

            # Generating image, it returns whether or not the image was generated
            valid = generate_image(j, info['path'], img_dir_path, img_path)
            if not valid:
                continue
            
            # Appending the image to the dataset
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            dataset_x.append(img)
            dataset_y.append(j)
        i += 2

# Saving the dataset to a numpy file
np.save("./dataset_x.npy", np.array(dataset_x).reshape(-1, width, height, 1))
np.save("./dataset_y.npy", np.array(dataset_y).reshape(-1, 1))
