from django.http import HttpResponse, HttpResponseNotFound
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from menu.models import *
from menu.permissions import IsAdminOrReadOnly
from menu.serializers import *


class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'price']
    permission_classes = [IsAdminOrReadOnly]


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]


# mainmenu = [{'title': 'Легенда', 'url_name': 'menu'},
#         {'title': 'Меню', 'url_name': 'menu'},
#         {'title': 'Забронировать стол', 'url_name': ''},
#         {'title': 'Контакты', 'url_name': 'contact'},
#         {'title': 'Отзывы', 'url_name': 'login'},
#         {'title': 'Войти', 'url_name': 'login'}
#         ]


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')