from django import views
from .views import *
from django.urls import path

urlpatterns = [
    path('', home_view, name="home_view"),
    path('tweets_list', tweets_list, name="tweets_list"),
    path('<int:tweet_id>/', tweet_detail_view, name="tweet_detail"),
]