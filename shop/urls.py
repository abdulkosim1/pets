from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('service', ServiceModelViewSet)
urlpatterns = [
    path('get_shop/', ShopListCreateAPIView.as_view()),

    path('get_shop_detail/<int:id>/', get_shop),

    path('', include(router.urls)),



]