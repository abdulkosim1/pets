from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.title


class Pets(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pets')
    title = models.CharField(max_length=40)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='pets')
    breed = models.CharField(max_length=20, blank=True, null=True, default='')
    image = models.ImageField(upload_to='pets_image')
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self) -> str:
        return f'{self.title} - {self.owner}'


