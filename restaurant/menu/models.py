from django.db import models
from django.urls import reverse


class FoodAndDrinks(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=None, null=True, verbose_name='Рейтинг')
    weight = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Граммовка')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')

    def __str__(self):
        return self.name


