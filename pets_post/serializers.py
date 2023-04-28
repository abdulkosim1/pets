from rest_framework import serializers
from .models import Pets, Category
from feedback.serializers import CommentSerializer
from main.settings import URL_SITE

class PetsSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)
    comments = CommentSerializer(many=True, read_only=True)
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = URL_SITE + instance.image.url
        return representation

    class Meta:
        model = Pets
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = URL_SITE + instance.image.url
        return representation
    class Meta:
        model = Pets
        fields = '__all__'

class CategoryAllSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'