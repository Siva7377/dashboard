from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import NewsArticle
from .serializers import NewsArticleSerializer

class NewsArticleViewSet(viewsets.ModelViewSet):
    queryset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerializer


def Dashboard(request):

    return  render(request,"home.html")