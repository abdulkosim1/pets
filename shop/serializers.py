from rest_framework import serializers
from .models import Shop, Service
from django.db.models import Avg


class ShopSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = 'http://34.89.184.22' + instance.image.url
        representation['ratings'] = instance.shop_ratings.aggregate(Avg('rating'))
        return representation
    class Meta:
        model = Shop
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    shop_code = serializers.CharField(required=True)
    # shop = ShopSerializer(required=False)

    def validate_shop_code(self, shop_code):
        if not Shop.objects.filter(shop_code=shop_code).exists():
            raise serializers.ValidationError('Неверный код!')
        return shop_code
    class Meta:
        model = Service
        fields = ('title', 'description', 'image', 'price', 'shop_code')