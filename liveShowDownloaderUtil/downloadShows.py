import pytube
from pytube import YouTube

def downloadShow(link, title, path):
    try:
        yt = YouTube(link)
        t = yt.streams.filter(only_audio=True)
        t[0].download(path, filename=title + ".mp3")
        print("Downloaded " + title)
    except:
        print("Failed to download " + title)
        pass