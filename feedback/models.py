from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from pets_post.models import Pets
from shop.models import Shop

User = get_user_model()

class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Pets, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.owner} --> {self.post.title}'
    
class Rating(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_ratings')
    shops = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='shop_ratings')
    rating = models.SmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
        blank=True, null=True
    )

    def __str__(self) -> str:
        return f'{self.owner} --> {self.shops.title}'
    

class Review(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    phone_number = models.CharField(max_length=30)
    theme = models.CharField(max_length=30)
    message = models.TextField()

    def __str__(self) -> str:
        return self.name