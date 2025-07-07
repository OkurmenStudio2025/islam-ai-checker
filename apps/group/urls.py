from django.urls import path
from .views import GroupListAPIView, GroupDetailAPIView


# URL patterns for the group app
urlpatterns = [
    path('groups/', GroupListAPIView.as_view(), name='groups-list'),
    path('groups/<int:id>/',
         GroupDetailAPIView.as_view(), name='groups-detail'),
]
