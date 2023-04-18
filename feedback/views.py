from .models import Comment, Rating, Review
from rest_framework.response import Response
from shop.models import Shop
from rest_framework.viewsets import ModelViewSet
from .serializers import CommentSerializer, RatingSerializer, ReviewSerializer
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from shop.serializers import ShopSerializer


class CommentModelViewSet(ModelViewSet): # CRUD на комменты
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)
        return serializer
    
class AddRating(CreateAPIView): # Post запрос на добавление рейтинга
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [IsAuthenticated, ]

    def post(self, request, pk, *args, **kwargs):
        serializer = RatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        rating_obj, _ = Rating.objects.get_or_create(owner=request.user, shops_id=pk)
        rating_obj.rating = request.data['rating']
        rating_obj.save()
        return Response(serializer.data)

class ReviewListCreateAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer