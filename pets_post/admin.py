from django.contrib import admin
from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import Category, Pets

# Register your models here.

admin.site.register(Category)
# admin.site.register(Pets)

class PetsAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner',)
    # fields = ['title']


    
admin.site.register(Pets, PetsAdmin)