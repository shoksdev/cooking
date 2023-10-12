from django.urls import path, include
from rest_framework import routers

from .views import DishesViewSet, CreateDishView

router = routers.SimpleRouter()
router.register(r'dishes', DishesViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('dishes/create', CreateDishView.as_view(), name='create_dish')
]
