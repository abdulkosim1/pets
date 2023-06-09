from django.contrib import admin
from .models import Shop, Service, Category

class ShopAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_confirmed',)
# Register your models here.

admin.site.register(Shop, ShopAdmin)
admin.site.register(Service)
admin.site.register(Category)