from pytube import YouTube, Playlist
from pathlib import Path
import os


def on_download_progress(stream, chunk, bytes_remaining):
    bytes_downloaded = stream.filesize - bytes_remaining
    percent = int(bytes_downloaded * 100 / stream.filesize)
    print(f"{percent}%")


def download_video(url):
    try:
        youtube_video = YouTube(url)
        p = Path.cwd()
        path = f"{p}/videos_youtube/{youtube_video.author}"
        os.makedirs(path, exist_ok=True)
        youtube_video.register_on_progress_callback(on_download_progress)
        stream = youtube_video.streams.get_highest_resolution()
        stream.download(path)
    except:
        print("Error")


def download_playlist(url):
    try:
        youtube_playlist = Playlist(url)
        owner = youtube_playlist.owner
        title = youtube_playlist.title
        p = Path.cwd()
        path = f"{p}/videos_youtube/{owner}/{title}"
        os.makedirs(path, exist_ok=True)
        for i, video in enumerate(youtube_playlist.videos, 1):
            print(f'Download videos n°{i}/{youtube_playlist.length}')
            video.register_on_progress_callback(on_download_progress)
            video.streams.get_highest_resolution().download(path)
    except:
        print("Error")


def is_playlist(url):
    if url.find("playlist") == -1:
        download_video(url)
    else:
        download_playlist(url)


url = input("Paste YouTube link : ")
is_playlist(url)
