from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

urlpatterns = [
    path('get_pets/', PetsListAPIView.as_view()),
    path('get_free_pets/', GetFreePetsListAPIView.as_view()),
    path('create_pets/', PetsCreateAPIView.as_view()),
    path('change/<int:id>/', PetsUpdateDestroyAPIView.as_view({'put': 'update','patch': 'partial_update','delete': 'destroy'})),
    path('get_pet/<int:id>/', get_pet),



]

