
# Kakiburi

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/) [![MIT License](https://img.shields.io/badge/Release-0.0.1-blue)](https://google.com)

Kakiburi is a dataset of computer generated japanese characters (60x60 grayscale, 423,023 images).

This dataset contains almost all used japanese characters ranging from hiragana, katakana and kanji to punctuation and special symbols.

It was made by generating 60x60 grayscale images using commercial use ok fonts.
## Downloading the dataset

You can download the dataset in a numpy array (.npy) format or download the images (.tar)

File | Images | Download (Numpy format) | Download (Archive format)
--- | --- | --- | --- |
Complete dataset | 423,023 | [kakiburi-dataset.tar.gz](https://github.com/Kizeko/Kakiburi/releases/download/Latest/kakiburi-dataset.tar.gz) (268MB)
    
## Generating the dataset

Dataset can be generated with docker or by cloning this repository.

## Docker

Docker image : https://hub.docker.com/repository/docker/kizeko/kakiburi

Running the container

```bash
  $ docker run -it --name kakiburi kizeko/kakiburi:latest
```

Keep in mind it takes a long time to generate that much images.
When it is done, you can transfer the data with :

```bash
  $ docker cp kakiburi:/app/dataset_x.npy destPath
  $ docker cp kakiburi:/app/dataset_y.npy destPath
```
## Locally

```bash
  $ git clone https://github.com/Kizeko/Kakiburi.git

  $ cd ./Kakiburi

  $ pip install -r requirements.txt

  $ python generate_data.py

```


## License

[MIT](https://choosealicense.com/licenses/mit/)

