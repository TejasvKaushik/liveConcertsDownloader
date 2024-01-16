from liveShowDownloaderUtil.getShowLinks import getShowLinks
from liveShowDownloaderUtil.downloadShows import downloadShow
import os

def main():
    print("Starting the liveShowDownloader")
    artist = input("Enter the name of the artist: ")
    links, titles = getShowLinks(artist)
    print(len(links))


    newPath = r'D:\Music\LiveConcerts\{}'.format(artist)
    if not os.path.exists(newPath):
        os.makedirs(newPath)
    print(newPath)

    # downloadShow(links[0], titles[0], newPath)

    for link, title in zip(links, titles):
        downloadShow(link, title, newPath)



if __name__ == "__main__":
    main()