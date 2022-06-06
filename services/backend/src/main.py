import subprocess
import tempfile
import pathlib
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import youtube_dl


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': '/downloads/%(title)s.%(ext)s'
}


@app.get("/")
def home():
    return "Hello, World!"


@app.get("/download/")
def download_video(url: str):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.cache.remove()
        info = ydl.extract_info(url)
        filename = ydl.prepare_filename(info)
        name, ext = os.path.splitext(filename)
        print("Filename:", name + ".mp3")
    return FileResponse(name + ".mp3")
