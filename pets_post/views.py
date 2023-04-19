from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics, mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Pets, Category
from .serializers import PetsSerializer, CategorySerializer, CategoryAllSerializer
from django.contrib.auth import get_user_model
from .permissions import IsOwner
from rest_framework.decorators import api_view
from rest_framework.response import Response

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
    filter_fields = ['owner', 'title', 'category']
    search_fields = ['title', ]
    ordering_fileds = ['id','owner',]

class CategoryListAPIView(generics.ListAPIView): # Просмотр category 
    queryset = Category.objects.all()
    serializer_class = CategoryAllSerializer
    permission_classes = []
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['title',]
    search_fields = ['title', ]

class PetsCreateAPIView(generics.CreateAPIView): # Добавление pets
    queryset = Pets.objects.all()
    serializer_class = PetsSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PetsUpdateDestroyAPIView(mixins.UpdateModelMixin,
                                    mixins.DestroyModelMixin,
                                    viewsets.GenericViewSet): # Удаление, изменение постов
    queryset = Pets.objects.all()
    serializer_class = PetsSerializer
    permission_classes = [IsAuthenticated, IsOwner,]
    lookup_field='id'

@api_view(['GET'])
def get_pet(request, id):
    try:
        pet = Pets.objects.get(id=id)
    except Pets.DoesNotExist:
        return Response('Pet does not exist')
    serializer = PetsSerializer(pet, many=False)
    return Response(serializer.data)
        
class GetFreePetsListAPIView(generics.ListAPIView): # Просмотр pets 
    serializer_class = PetsSerializer
    permission_classes = []
    queryset = Pets.objects.filter(price=0)

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['owner', 'title',]
    search_fields = ['title', ]
    ordering_fileds = ['id','owner',]

@api_view(['GET'])
def get_pet_category(request, pk):
    try:
        category = Category.objects.get(pk=pk)
        pets_in_category = category.pets.all()
    except Category.DoesNotExist:
        return Response('Category does not exist')
    serializer = CategorySerializer(pets_in_category, many=True)
    return Response(serializer.data)

