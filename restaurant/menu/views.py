from django.http import HttpResponse, HttpResponseNotFound
from rest_framework.viewsets import ModelViewSet

from menu.models import *
from menu.serializers import *


class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# mainmenu = [{'title': 'Легенда', 'url_name': 'menu'},
#         {'title': 'Меню', 'url_name': 'menu'},
#         {'title': 'Забронировать стол', 'url_name': ''},
#         {'title': 'Контакты', 'url_name': 'contact'},
#         {'title': 'Отзывы', 'url_name': 'login'},
#         {'title': 'Войти', 'url_name': 'login'}
#         ]


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')