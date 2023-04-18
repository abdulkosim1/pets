from rest_framework import serializers
from .models import Rating, Comment, Review


class RatingSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = Rating
        fields = ('rating',)

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    def to_representation(self, instance):
        representation =  super().to_representation(instance)

            # representation['profile_image'] = instance.owner.profile_image.url
        return representation


    class Meta:
        model = Comment
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'