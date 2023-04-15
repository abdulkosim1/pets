from django.contrib import admin
from .models import Category, Pets

class PetsAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner',)

admin.site.register(Category)    
admin.site.register(Pets, PetsAdmin)