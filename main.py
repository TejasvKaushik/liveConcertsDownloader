from liveShowDownloaderUtil.getShowLinks import getShowLinks
from liveShowDownloaderUtil.downloadShows import downloadShow
import path as path
import os
import tkinter as tk
import customtkinter as ctk

# finishLabel = None

def findLiveShows(artist, finishLabel):
    # global finishLabel
    links, titles = getShowLinks(artist)
    searchResults = f"Live shows found: {len(links)}"
    finishLabel.configure(text=searchResults)

def main():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")

    app = ctk.CTk()
    app.title("Live Show Downloader")
    app.geometry("720x480")

    title = ctk.CTkLabel(app, text="Enter an artist or a band", font=("Arial", 20))
    title.pack(padx=10, pady=10, fill=tk.X, expand=True)

    # artist input
    artist = tk.StringVar()
    link = ctk.CTkEntry(app, textvariable=artist, font=("Arial", 20))
    link.pack(padx=10, pady=10, fill=tk.X, expand=True)

    # finish label
    finishLabel = ctk.CTkLabel(app, text="", font=("Arial", 20))
    finishLabel.pack()

    # find live shows button
    findLiveShowsButton = ctk.CTkButton(app, text="Find Live Shows", font=("Arial", 20), command=lambda: findLiveShows(artist.get(), finishLabel))
    findLiveShowsButton.pack(padx=10, pady=10, fill=tk.X, expand=True)

    # print("Starting the liveShowDownloader")
    # artist = input("Enter the name of the artist: ")
    

    # newPath = r'D:\Music\LiveConcerts\{}'.format(artist)
    # basePath = path.BASE_PATH
    # newPath = basePath + artist
    # if not os.path.exists(newPath):
    #     os.makedirs(newPath)
    # print(newPath)

    # # downloadShow(links[0], titles[0], newPath)


    # for link, title in zip(links, titles):
    #     downloadShow(link, title, newPath)


    # run app
    app.mainloop()

if __name__ == "__main__":
    main()