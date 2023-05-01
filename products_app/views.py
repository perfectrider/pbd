from rest_framework import generics, permissions
from .models import Assortment, Division
from .serializers import AssortmentSerializer, DivisiontSerializer


class AssortmentListView(generics.ListCreateAPIView):
    queryset = Assortment.objects.all()
    serializer_class = AssortmentSerializer
    permission_classes = [permissions.IsAuthenticated]


class DivisionListView(generics.ListCreateAPIView):
    queryset = Division.objects.all()
    serializer_class = DivisiontSerializer
    permission_classes = [permissions.IsAuthenticated]
