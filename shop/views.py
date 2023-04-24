from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from pets_post.views import CustomPagination
from .models import Shop, Service
from .serializers import ShopSerializer, ServiceSerializer
from rest_framework.response import Response


# Create your views here.

class ShopListCreateAPIView(generics.ListCreateAPIView): # Просмотр shops 
    queryset = Shop.objects.filter(is_confirmed=True)
    serializer_class = ShopSerializer
    permission_classes = []
    pagination_class = CustomPagination

@api_view(['GET'])
def get_shop(request, id):
    try:
        pet = Shop.objects.get(id=id)
    except Shop.DoesNotExist:
        return Response('Shop does not exist')
    serializer = ShopSerializer(pet, many=False)
    return Response(serializer.data)


class ServiceModelViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def perform_create(self, serializer):
        serializer.save(shop=self.request.shop)
        return serializer
