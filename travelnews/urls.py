from django.urls import path
from .views import get_travel_news

urlpatterns = [
    path('api/travel-news/', get_travel_news, name='travel-news'),
]