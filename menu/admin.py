from django.contrib import admin
from django.contrib.admin import ModelAdmin


from menu.models import Menu, Category


@admin.register(Menu)
class MenuAdmin(ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    pass
