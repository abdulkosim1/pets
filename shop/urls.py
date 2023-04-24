from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('service', ServiceModelViewSet)
urlpatterns = [
    path('get_shop/', ShopListCreateAPIView.as_view()),

    path('get_shop_detail/<int:id>/', get_shop),
    path('get_shop_category/<int:pk>/', get_shop_category),

    path('', include(router.urls)),



]