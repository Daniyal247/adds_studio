from django.shortcuts import render
from rest_framework import viewsets
from .models import ContentItem
from .serializers import ContentItemSerializer

# Create your views here.

class ContentItemViewSet(viewsets.ModelViewSet):
    queryset = ContentItem.objects.all()
    serializer_class = ContentItemSerializer