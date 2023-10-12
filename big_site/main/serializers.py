from rest_framework.serializers import ModelSerializer

from .models import Dishes


class DishesSerializer(ModelSerializer):
    class Meta:
        model = Dishes
        fields = '__all__'
