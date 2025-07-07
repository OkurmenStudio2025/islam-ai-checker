from django.urls import path
from .views import HomeworkReviewCreateAPIView

urlpatterns = [
    path('homework/', HomeworkReviewCreateAPIView.as_view()),        # POST
    path('homework/<int:pk>/', HomeworkReviewCreateAPIView.as_view()),  # GET by ID
]
