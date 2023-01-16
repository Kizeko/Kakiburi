
# Kakiburi

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/) [![MIT License](https://img.shields.io/badge/Release-0.0.4-blue)](https://google.com)

Kakiburi is a dataset of computer generated japanese characters (60x60 grayscale) that comes in 2 flavors (382,878 images, 8298 chars) or (369,098 images, 7110 chars).

This dataset contains japanese characters ranging from hiragana, katakana and kanji to punctuation and special symbols.

It was made by generating 60x60 grayscale images using commercial use ok fonts.
## Downloading the dataset

You can download the dataset in a numpy array (.npy) format.

File | Images | Unique characters | Download (Numpy format)
--- | --- | --- | --- |
dataset_10 | 382,878 | 8298 | [dataset_10.tar.gz](https://github.com/Kizeko/Kakiburi/releases/download/0.0.4/dataset_10.tar.gz) (451MB)
dataset_15 | 369,098 | 7110 | [dataset_15.tar.gz](https://github.com/Kizeko/Kakiburi/releases/download/0.0.4/dataset_15.tar.gz) (435MB)
    
## Generating the dataset

Dataset can be generated with docker or by cloning this repository.

## Docker

Docker image : https://hub.docker.com/repository/docker/kizeko/kakiburi

Running the container

```bash
  $ docker run -it --name kakiburi -v "/custom/path:/data" kizeko/kakiburi:latest
```
Example :

```bash
  $ docker run -it --name kakiburi -v "~/kakiburi:/data" kizeko/kakiburi:latest
```

Keep in mind it takes a long time to generate that much images.

## Locally

```bash
  $ git clone https://github.com/Kizeko/Kakiburi.git

  $ cd ./Kakiburi

  $ pip install -r requirements.txt

  $ python generate_data.py

```


## License

[MIT](https://choosealicense.com/licenses/mit/)

