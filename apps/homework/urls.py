from django.urls import path
from .views import HomeworkReviewCreateAPIView

urlpatterns = [
    path('homework/', HomeworkReviewCreateAPIView.as_view(), name='homework'),
]
