import pytube
from pytube import YouTube
import os

def downloadShow(link, title, path):
    try:
        yt = YouTube(link)
        t = yt.streams

        videoPath = path + '\\video'
        print(videoPath)
        if not os.path.exists(videoPath):
            os.makedirs(videoPath)

        t[0].download(videoPath, filename=title + ".mp4")
        print("Video Downloaded " + title)

        audioPath = path + '\\audio'
        print(audioPath)
        if not os.path.exists(audioPath):
            os.makedirs(audioPath)
        
        t.filter(only_audio=True)
        t[0].download(audioPath, filename=title + ".mp3")
        print("Audio Downloaded " + title)
    except:
        print("Failed to download " + title)
        pass