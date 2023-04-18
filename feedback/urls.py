from django.urls import path, include
from feedback.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('comment', CommentModelViewSet)

urlpatterns = [  # adding , rating
    path('<int:pk>/rating/', AddRating.as_view()),
    path('review/', ReviewListCreateAPIView.as_view()),

    path('', include(router.urls)),
]