from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Tweet
from .serializers import TweetSerializer


class TweetList(generics.ListCreateAPIView):
  queryset = Tweet.objects.all()
  serializer_class = TweetSerializer
  permission_classes = [AllowAny,]


def index(request):
  context = {}
  return render(request, 'tweet/index.html')
