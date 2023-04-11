from django.urls import path
from .views import *

urlpatterns = [
    path('get_pets/', PetsListAPIView.as_view()),
    path('create_pets/', PetsCreateAPIView.as_view()),
    path('change/<int:id>/', PetsRetriveUpdateDestroyAPIView.as_view()),


]