from rest_framework.routers import DefaultRouter
from .views import HomeworkViewSet, HomeworkReviewCreateAPIView
from django.urls import path, include


router = DefaultRouter()
router.register(r'homework-results', HomeworkViewSet, basename='homework-result')

urlpatterns = [
    path('homework/', HomeworkReviewCreateAPIView.as_view(), name='homework-review'),
    path('', include(router.urls)),
]
