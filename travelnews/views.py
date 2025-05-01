from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def get_travel_news(request):
    url = "https://newsapi.org/v2/everything?q=travel&apiKey=5c70a4b09c114d5387cfeb30c9af0da2"
    params = {
        'q': 'beautiful places to visit',
        'apiKey': '5c70a4b09c114d5387cfeb30c9af0da2',
        'language': 'en',
        'sortBy': 'publishedAt',
        'apikey': '5c70a4b09c114d5387cfeb30c9af0da2',
    }
    response = requests.get(url, params=params)
    data = response.json()

    return JsonResponse(data)

