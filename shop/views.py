from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from pets_post.views import CustomPagination
from .models import Shop, Service, Category
from .serializers import ShopSerializer, ServiceSerializer, CategorySerializer
from rest_framework.response import Response

class ShopListCreateAPIView(generics.ListCreateAPIView): # Просмотр shops 
    queryset = Shop.objects.filter(is_confirmed=True)
    serializer_class = ShopSerializer
    permission_classes = []
    pagination_class = CustomPagination

class ServiceModelViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


@api_view(['GET'])
def get_shop(request, id):
    try:
        pet = Shop.objects.get(id=id)
    except Shop.DoesNotExist:
        return Response('Shop does not exist')
    serializer = ShopSerializer(pet, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def get_shop_category(request, pk):
    try:
        category = Category.objects.get(pk=pk)
        shops_in_category = category.category_shop.filter(is_confirmed=True)
    except Category.DoesNotExist:
        return Response('Category does not exist')
    serializer = ShopSerializer(shops_in_category, many=True)
    return Response(serializer.data)
