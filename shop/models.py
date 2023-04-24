from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from account.send_email import send_email_about_shop

User = get_user_model()

class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.title

class Shop(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_shop')
    description = models.TextField()
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    social_net = models.CharField(max_length=50)
    image = models.ImageField(upload_to='shop_images')

    is_confirmed = models.BooleanField(default=False)
    shop_code = models.CharField(max_length=50, blank=True)

    def create_shop_code(self):
        import uuid
        code = str(uuid.uuid4())
        self.shop_code = code

    def __str__(self) -> str:
        return self.title
    

class Service(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='service')
    title = models.CharField(max_length=40)
    description = models.TextField()
    image = models.ImageField(upload_to='service/')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self) -> str:
        return self.title

    
@receiver(post_save, sender=Shop)
def shop_create(sender, instance, created, **kwargs):
    if created:
        for user in User.objects.filter(is_staff=True):
            send_email_about_shop(user.email)




        
        
