from rest_framework import serializers
from .models import Pets


class PetsSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)

    class Meta:
        model = Pets
        fields = '__all__'

