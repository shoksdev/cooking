from django.shortcuts import render
from rest_framework import mixins
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import GenericViewSet

from .models import Dishes
from .serializers import DishesSerializer


class CreateDishView(CreateAPIView):
    queryset = Dishes.objects.all()
    serializer_class = DishesSerializer


class DishesViewSet(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    queryset = Dishes.objects.all()
    serializer_class = DishesSerializer
