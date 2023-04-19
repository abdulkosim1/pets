from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from account.send_email import send_email_about_shop

User = get_user_model()

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
    

# class Service(models.Model):
#     shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='service')

    
@receiver(post_save, sender=Shop)
def shop_create(sender, instance, created, **kwargs):
    if created:
        for user in User.objects.filter(is_staff=True):
            send_email_about_shop(user.email)




        
        
