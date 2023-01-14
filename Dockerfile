FROM python:3.8.13

WORKDIR /app

COPY . .

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y

RUN pip install -r requirements.txt

CMD ["python", "generate_dataset.py"]