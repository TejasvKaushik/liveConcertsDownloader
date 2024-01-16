import pytube
from pytube import YouTube
from pytube import Search

def getShowLinks(name):
    links = []
    titles = []
    searchResults = Search(name + " live")
    searchResults.results
    searchResults.get_next_results()

    for i in searchResults.results:
        if(i.length > 3000):
            links.append(i.watch_url)
            titles.append(i.title)

    return links, titles