import pytube
from pytube import YouTube
from pytube import Search

def getShowLinks(name):
    try: 
        links = []
        titles = []
        searchResults = Search(name + " live")
        print("found search results")
        searchResults.results
        searchResults.get_next_results()
        print("got next results")

        for i in searchResults.results:
            if(i.length > 3000):
                links.append(i.watch_url)
                titles.append(i.title)
                print("Added")

        return links, titles
    except:
        print("Failed to get links")
        pass