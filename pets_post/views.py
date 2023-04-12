from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Pets
from .serializers import PetsSerializer
from django.contrib.auth import get_user_model
from .permissions import IsOwner

User = get_user_model()


class CustomPagination(PageNumberPagination): # Кастомная пагинация
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 20

class PetsListAPIView(generics.ListAPIView): # Просмотр pets 
    queryset = Pets.objects.all()
    serializer_class = PetsSerializer
    permission_classes = []
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['owner', 'title',]
    search_fields = ['title', ]
    ordering_fileds = ['id','owner',]

class PetsCreateAPIView(generics.CreateAPIView): # Добавление pets
    queryset = Pets.objects.all()
    serializer_class = PetsSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PetsRetriveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView): # Удаление, изменение постов
    queryset = Pets.objects.all()
    serializer_class = PetsSerializer
    permission_classes = [IsAuthenticated, IsOwner,]
    lookup_field='id'
        
class GetFreePetsListAPIView(generics.ListAPIView): # Просмотр pets 
    serializer_class = PetsSerializer
    permission_classes = []
    queryset = Pets.objects.filter(price=0)

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['owner', 'title',]
    search_fields = ['title', ]
    ordering_fileds = ['id','owner',]


