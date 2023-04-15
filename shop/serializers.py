from rest_framework import serializers
from .models import Shop
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