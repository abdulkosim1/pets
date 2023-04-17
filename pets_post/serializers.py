from rest_framework import serializers
from .models import Pets, Category

class PetsSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = 'http://34.89.184.22' + instance.image.url
        return representation

    class Meta:
        model = Pets
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = 'http://34.89.184.22' + instance.image.url
        return representation
    class Meta:
        model = Pets
        fields = '__all__'