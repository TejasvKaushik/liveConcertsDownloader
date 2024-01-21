from liveShowDownloaderUtil.getShowLinks import getShowLinks
from liveShowDownloaderUtil.downloadShows import downloadShow
import path as path
import os
import tkinter as tk
import customtkinter as ctk
import time

# finishLabel = None

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("Live Show Downloader")
app.geometry("720x480")

def findLiveShows(artist, finishLabel, linksAndTitles):
    # global finishLabel
    links, titles = getShowLinks(artist)

    for link, title in zip(links, titles):
        linksAndTitles[title] = link

    searchResults = f"Found {len(links)} shows for {artist}"
    finishLabel.configure(text=searchResults)

    if linksAndTitles:
        linksAndTitlesFrame = ctk.CTkScrollableFrame(app)
        linksAndTitlesFrame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        linksAndTitlesLabel = ctk.CTkLabel(linksAndTitlesFrame, text=artist, font=("Arial", 20))
        linksAndTitlesLabel.pack(fill=tk.X, expand=True)

        linksAndTitlesListbox = ctk.CTkTextbox(linksAndTitlesFrame, font=("Arial", 20))
        linksAndTitlesListbox.pack(fill=tk.BOTH, expand=True)

        for title, link in linksAndTitles.items():
            linksAndTitlesListbox.insert(tk.END, title)
            linksAndTitlesListbox.insert(tk.END, "\n")




def main():
    

    title = ctk.CTkLabel(app, text="Enter an artist or a band", font=("Arial", 20))
    title.pack(padx=10, pady=10)

    # artist input
    artist = tk.StringVar()
    link = ctk.CTkEntry(app, textvariable=artist, font=("Arial", 20))
    link.pack(padx=10, pady=10, fill=tk.X)

    # dict to store links and titles
    linksAndTitles = {}

    # finish label
    finishLabel = ctk.CTkLabel(app, text="", font=("Arial", 20))
    finishLabel.pack()

    # find live shows button
    findLiveShowsButton = ctk.CTkButton(app, text="Find Live Shows", font=("Arial", 20), command=lambda: findLiveShows(artist.get(), finishLabel, linksAndTitles={}))
    findLiveShowsButton.pack(padx=10, pady=5)

    # links and titles
    
    


    # if linksAndTitles:
    #     # display links and titles
    #     linksAndTitlesFrame = ctk.CTkFrame(app)
    #     linksAndTitlesFrame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    #     linksAndTitlesLabel = ctk.CTkLabel(linksAndTitlesFrame, text="Links and Titles", font=("Arial", 20))
    #     linksAndTitlesLabel.pack(fill=tk.X, expand=True)

    #     linksAndTitlesListbox = ctk.CTkTextbox(linksAndTitlesFrame, font=("Arial", 20))
    #     linksAndTitlesListbox.pack(fill=tk.BOTH, expand=True)

    #     for title, link in linksAndTitles.items():
    #         linksAndTitlesListbox.insert(tk.END, title)

    

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