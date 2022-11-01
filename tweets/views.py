from ast import ExceptHandler
from django.shortcuts import render
from django.http import Http404, HttpResponse, JsonResponse
from .models import *
from .serializers import TweetSerializer
from rest_framework.exceptions import APIException

# Create your views here.
# def add_data():
#     obj = Tweet()
#     obj.content = "Hello World 3"
#     obj.save()

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    # add_data()
    obj = Tweet.objects.all().order_by('-tweet_creation_date')
    serializer = TweetSerializer(obj, many=True)
    print("obj: ", obj)
    return render(request, "pages/home.html", context={'obj':serializer.data}, status=200)

def tweets_list(request, *args, **kwargs):
    obj = Tweet.objects.all().order_by('-tweet_creation_date')
    serializer = TweetSerializer(obj, many=True)
    return JsonResponse(serializer.data, safe=False)

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    try:
        obj = Tweet.objects.get(id=tweet_id)
        serializer = TweetSerializer(obj, many=False)
        msg = serializer.data
    except :
        msg = {"status_code":404, 'msg':'Not Found'}
    return JsonResponse(msg)