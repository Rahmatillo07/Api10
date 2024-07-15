from django.shortcuts import render

from .models import Cost
from .serializers import CostSerializer
from .permissions import UserPermission

from rest_framework.viewsets import ModelViewSet


class CostApiView(ModelViewSet):
    queryset = Cost.objects.all()
    serializer_class = CostSerializer
    permission_classes = [UserPermission]
