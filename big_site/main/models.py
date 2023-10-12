from django.contrib.auth.models import User
from django.db import models


class Types(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название типа')

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

    def __str__(self):
        return self.title


class Kitchens(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название национальной кухни')

    class Meta:
        verbose_name = 'Кухня'
        verbose_name_plural = 'Кухни'

    def __str__(self):
        return self.title


class Celebrations(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название праздника')

    class Meta:
        verbose_name = 'Праздник'
        verbose_name_plural = 'Праздники'

    def __str__(self):
        return self.title


class Ages(models.Model):
    title = models.CharField(max_length=50, verbose_name='Возраст')

    class Meta:
        verbose_name = 'Возраст'
        verbose_name_plural = 'Возраста'

    def __str__(self):
        return self.title


class Purposes(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название предназначения')

    class Meta:
        verbose_name = 'Предназначение'
        verbose_name_plural = 'Предназначения'

    def __str__(self):
        return self.title


class Dishes(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(max_length=300, verbose_name='Описание')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')
    ingredients = models.TextField(max_length=600, verbose_name='Ингридиенты')
    type = models.ForeignKey(Types, on_delete=models.CASCADE, verbose_name='Тип')
    kitchen = models.ForeignKey(Kitchens, on_delete=models.CASCADE, verbose_name='Национальная кухня')
    celebration = models.ForeignKey(Celebrations, on_delete=models.CASCADE, verbose_name='Праздник')
    age = models.ForeignKey(Ages, on_delete=models.CASCADE, verbose_name='Возраст')
    purpose = models.ForeignKey(Purposes, on_delete=models.CASCADE, verbose_name='Предназначение')
    quantity = models.IntegerField(default=0, verbose_name='Количество порций')
    caloric_value = models.IntegerField(default=0, verbose_name='Количество калорий')
    proteins = models.IntegerField(default=0, verbose_name='Количество белков')
    fats = models.IntegerField(default=0, verbose_name='Количество жиров')
    carbohydrates = models.IntegerField(default=0, verbose_name='Количество углеводов')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return self.title
