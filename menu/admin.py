from django.contrib import admin
from django.contrib.admin import ModelAdmin


from menu.models import Menu


@admin.register(Menu)
class MenuAdmin(ModelAdmin):
    pass
