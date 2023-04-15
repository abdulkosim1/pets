from django.contrib import admin
from .models import Category, Pets

# Register your models here.

admin.site.register(Category)
# admin.site.register(Pets)

class PetsAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner',)
    # fields = ['title']


    
admin.site.register(Pets, PetsAdmin)