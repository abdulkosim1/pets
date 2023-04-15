from django.urls import path
from .views import *
urlpatterns = [
    path('get_shop/', ShopListCreateAPIView.as_view()),
    path('get_shop_detail/<int:id>/', get_shop),


]