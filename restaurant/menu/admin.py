from django.contrib import admin
from django.contrib.admin import ModelAdmin


from menu.models import Food


@admin.register(Food)
class MenuAdmin(ModelAdmin):
    pass
