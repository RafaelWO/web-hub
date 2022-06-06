FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY src/ /app

# Dir for downloads
RUN mkdir /downloads

RUN apt-get update
RUN apt-get install -y ffmpeg
