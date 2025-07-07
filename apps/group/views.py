from rest_framework import generics
from .models import Group
from .serializers import GroupSerializer


# This view retrieves a list of all groups
class GroupListAPIView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# This view retrieves a single group by its ID
class GroupDetailAPIView(generics.RetrieveAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    lookup_field = 'id'
