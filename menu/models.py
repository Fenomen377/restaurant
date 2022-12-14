from django.db import models
from django.urls import reverse


class Menu(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    price = models.IntegerField(verbose_name='Цена')
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=None, null=True, verbose_name='Рейтинг')
    weight = models.IntegerField(verbose_name='Граммовка')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'pots_id': self.pk})

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категория"


class Comment(models.Model):
    name = models.CharField(max_length=25, verbose_name='Имя')
    body = models.TextField(max_length=200, verbose_name='Ваш отзыв')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.name
