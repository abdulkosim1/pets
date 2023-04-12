from django.shortcuts import render
from rest_framework import generics
from pets_post.views import CustomPagination
from .models import Shop
from .serializers import ShopSerializer
# Create your views here.

class ShopListCreateAPIView(generics.ListCreateAPIView): # Просмотр pets 
    queryset = Shop.objects.filter(is_confirmed=True)
    serializer_class = ShopSerializer
    permission_classes = []
    pagination_class = CustomPagination

