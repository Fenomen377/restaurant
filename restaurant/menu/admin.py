from django.contrib import admin
from django.contrib.admin import ModelAdmin


from menu.models import FoodAndDrinks


@admin.register(FoodAndDrinks)
class MenuAdmin(ModelAdmin):
    pass
