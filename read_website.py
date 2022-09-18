import requests
from bs4 import BeautifulSoup

def read_web(input):
    name = input + " ott"
    url = 'https://www.google.com/search?q='+name
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    
    urls = []
    for link in soup.find_all('a'):
        urls.append(link.get('href'))
    print(urls)

    ott = ["hotstar","netflix","primevideo","sonyliv","zee5","voot","lionsgate","mxplayer","hulu"]
    names=[]
    for i in urls:
        for j in ott:
            if j in str(i):
                names.append(j)
    if names:
        return list(set(names))
    else:
        return "MOVIE IS NOT AVAILABLE ON ANY OTT PLATFORMS"
