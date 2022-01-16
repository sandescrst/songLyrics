from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.
def home(request):
    
    
    return render(request, 'homepage/home.html')

def lyrics(request):
    artist_name = str(request.GET.get('artist_name'))
    song = str(request.GET.get('song'))
    apiurl= 'https://api.lyrics.ovh/v1/' + artist_name + '/' + song
    req = requests.get(apiurl)
    json_data= req.json()['lyrics']
    return render(request, 'homepage/lyrics.html',{'lyric': json_data})
