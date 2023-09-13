from django.shortcuts import render

from rest_framework import views
from rest_framework.response import Response

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
                names.append(j.upper())
    print(names)
    if names:
        return list(set(names))
    else:
        return ['NO RESULT']

class OttSearchView(views.APIView):

    def post(self, request):
        name = request.data['name']
        print(name)
        data = read_web(name)
        data = {
            'name':data
        }
        
        print(type(data))
        return Response(data)