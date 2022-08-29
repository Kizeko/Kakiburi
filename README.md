
# Kakiburi

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/) [![MIT License](https://img.shields.io/badge/Release-0.0.1-blue)](https://google.com)

IN CONSTRUCTION

Kakiburi is a dataset of computer generated japanese characters (60x60 grayscale, 300,000 images).

This dataset contains almost all used japanese characters ranging from hiragana, katakana and kanji to punctuation and special symbols.

It was made by generating 60x60 grayscale images using commercial use ok fonts.
## Downloading the dataset

You can download the dataset in a numpy array (.npy) format or download the images (.tar)

File | Images | Download (Numpy format) | Download (Archive format)
--- | --- | --- | --- |
Complete dataset | 300,000 | [kakiburi-dataset.npy](https://google.com) (300MB) | [kakiburi-dataset.tar](https://google.com) (300MB)
Training images | 240,000 | [kakiburi-training-images.npy](https://google.com) (300MB) | [kakiburi-training-images.tar](https://google.com) (300MB) |
Training labels | 240,000 | [kakiburi-training-labels.npy](https://google.com) (300MB) | [kakiburi-training-labels.tar](https://google.com) (300MB)
Validation images | 60,000 | [kakiburi-validation-images.npy](https://google.com) (300MB) | [kakiburi-validation-images.tar](https://google.com) (300MB) |
Validation labels | 60,000 | [kakiburi-validation-labels.npy](https://google.com) (300MB) | [kakiburi-validation-labels.tar](https://google.com) (300MB)
    
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
  $ docker cp kakiburi:/app/<data> ~/Documents/Kakiburi
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

