from django.urls import path, include
from feedback.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('comment', CommentModelViewSet)

urlpatterns = [  # adding , rating
    path('<int:pk>/rating/', AddRating.as_view()),
    path('create_review/', ReviewCreateAPIView.as_view()),
    path('get_review/', ReviewListAPIView.as_view()),

    path('', include(router.urls)),
]