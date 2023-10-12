from django.contrib import admin

from .models import Dishes, Purposes, Ages, Celebrations, Kitchens, Types


@admin.register(Types)
class TypesAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Kitchens)
class KitchensAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Celebrations)
class CelebrationsAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Ages)
class AgesAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Purposes)
class PurposesAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Dishes)
class DishesAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'kitchen', 'celebration', 'age', 'purpose',)
