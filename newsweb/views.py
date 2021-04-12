import requests
import json
from django.shortcuts import render

# Create your views here.

def home(request):
    news_api_request = requests.get("http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=02b9be22b44a4901baa62c02fcd8bb14")
    api = json.loads(news_api_request.content)
    return render(request, 'top.html', {'api':api})

def entertainment(request):
    news_api_request = requests.get("http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=02b9be22b44a4901baa62c02fcd8bb14")
    api = json.loads(news_api_request.content)
    return render(request, 'ent.html', {'api':api})

def health(request):
    new_api_request = requests.get("http://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=02b9be22b44a4901baa62c02fcd8bb14")
    api = json.loads(new_api_request.content)
    return render(request, 'health.html', {'api':api})

def science(request):
    new_api_request = requests.get("http://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=02b9be22b44a4901baa62c02fcd8bb14")
    api = json.loads(new_api_request.content)
    return render(request, 'science.html', {'api':api})

def sport(request):
    new_api_request = requests.get("http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=02b9be22b44a4901baa62c02fcd8bb14")
    api = json.loads(new_api_request.content)
    return render(request, 'sport.html', {'api':api})
