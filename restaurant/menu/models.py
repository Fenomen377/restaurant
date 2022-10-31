from django.db import models
from django.urls import reverse


class Food(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=9, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=None, null=True)
    weight = models.DecimalField(max_digits=9, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']
