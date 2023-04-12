from django.db import models

# Create your models here.

class Shop(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=30)
    description = models.TextField()
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    social_net = models.CharField(max_length=50)
    image = models.ImageField(upload_to='shop_images')

    is_confirmed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title