
from django.shortcuts import render
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from articles.models import Article
from rest_framework.permissions import IsAuthenticated
from .serializers import ArticleSerializer

# Create your views here.
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsOwnerOrReadOnly,)