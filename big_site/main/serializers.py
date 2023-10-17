from rest_framework import serializers

from .models import Dishes


class DishesSerializer(serializers.ModelSerializer):
    new_ingredients = serializers.SerializerMethodField(method_name='get_new_ingredients')

    class Meta:
        model = Dishes
        fields = '__all__'

    def get_new_ingredients(self, dish_item=Dishes):
        ingredients = dish_item.ingredients
        ingredients_dict = {}
        ingredients_dict_new = {}
        for name in ingredients.split('\n'):
            key, *value = name.split('-')
            ingredients_dict[key] = value
        for key, value in ingredients_dict.items():
            new_key, new_value = key.strip(), value[0].strip()
            ingredients_dict_new[new_key] = new_value

        return ingredients_dict_new
