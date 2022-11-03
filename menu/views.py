from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from menu.models import *
from menu.permissions import IsAdminOrReadOnly
from menu.serializers import *


class MenuViewSetPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page_size'
    max_page_size = 20


class CategoryViewSetPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page_size'
    max_page_size = 20


class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'price']
    permission_classes = [IsAdminOrReadOnly]

    def get_paginated_response(self, data):
        return Response(data)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_paginated_response(self, data):
        return Response(data)


# menu = ['Легенда', 'Меню', 'Забронировать стол', 'Контакты', 'Отзывы', 'Войти']

menu = [{'title': "Легенда", 'url_name': 'legends'},
        {'title': "Меню", 'url_name': 'menu'},
        {'title': "Забронировать стол", 'url_name': 'table_reservation'},
        {'title': "Контакты", 'url_name': 'contacts'},
        {'title': "Отзывы", 'url_name': 'reviews'},
        {'title': "Войти", 'url_name': 'auth'}
        ]


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def index(request):
    posts = Menu.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная - ГамарджобаГенацвале'
    }
    return render(request, 'menu/index.html', context=context)


def auth(request):
    return render(request, 'menu/oauth.html', {'title': 'Авторизация'})


def legends(request):
    context ={
        'menu': menu,
        'title': 'Легенда'
    }
    return render(request, 'menu/legends.html', context=context)


def menu(request):
    posts = Menu.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Меню'
    }
    return render(request, 'menu/index.html', context=context)


def contacts(request):
    return HttpResponse('Контакты')


def reviews(request):
    return HttpResponse('Отзывы')


def table_reservation(request):
    return HttpResponse('Бронирование столика')




