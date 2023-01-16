import numpy as np
import pandas as pd
from tqdm.auto import tqdm

from csvscript import *
from font_util import *

# Import the generated csv file containing the fonts information
infos = pd.read_csv("./fonts.csv", index_col=0)

# Datasets
dataset_x = []
dataset_y = []

temp_dataset_x = []
temp_dataset_y = []

# Generate the dataset
i = 0
current_unicode_total_count = 0
cumulative_unicode_count = 0
while i < len(unicodes) - 1:
    start = unicodes[i]
    end = unicodes[i + 1]
    print("\nStarted Generating the part (U+{})-(U+{}) of the dataset :".format(hex(start)[2:], hex(end)[2:]))
    for j in (bar := tqdm(range(start, end))):
        bar.set_description("Generating {} (#{}). Total dataset size = {} ".format(chr(j), cumulative_unicode_count, len(dataset_x)))
        for index, info in infos.iterrows():
            # Path of the image directory that will be generated
            img_dir_path = "./images/U+{}".format(hex(j)[2:])
            # Path of the image that will be generated
            img_path = img_dir_path + "/{}_{}.png".format(hex(j)[2:], index)

            # Generating image, it returns whether or not the image was generated
            valid, image = generate_image(j, info['path'], img_dir_path, img_path)
            if not valid:
                continue
            
            # Appending the image to the dataset
            temp_dataset_x.append(image.getdata())
            temp_dataset_y.append(j)
            current_unicode_total_count += 1

        # If there is more than x images for this unicode, we add them to the dataset
        if current_unicode_total_count >= MIN_NUMBER_OF_IMAGES_PER_UNICODE:
            dataset_x.extend(temp_dataset_x)
            dataset_y.extend(temp_dataset_y)


        # Resetting the temporary dataset
        temp_dataset_x = []
        temp_dataset_y = []

        # Reseting current unicode count
        current_unicode_total_count = 0
        cumulative_unicode_count += 1
    i += 2

# Saving the dataset to a numpy file
np.save("../data/dataset_x.npy", np.array(dataset_x).reshape(-1, width, height, 1))
np.save("../data/dataset_y.npy", np.array(dataset_y).reshape(-1, 1))

print("Dataset generated successfully !")
