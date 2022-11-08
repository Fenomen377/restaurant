from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
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


menu = [{'title': "Легенда", 'url_name': 'legends'},
        {'title': "Забронировать стол", 'url_name': 'table_reservation'},
        {'title': "Контакты", 'url_name': 'contacts'},
        {'title': "Отзывы", 'url_name': 'reviews'},]
        # {'title': "Войти", 'url_name': 'auth'}]


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class MenuHome(ListView):
    model = Menu
    template_name = 'menu/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница - ГамарджобаГенацвале'
        context['category_selected'] = 0
        return context


class ShowCategory(ListView):
    model = Menu
    template_name = 'menu/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Menu.objects.filter(category__id=self.kwargs['category_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Категория - ' + str(context['posts'][0].category)
        context['category_selected'] = context['posts'][0].category_id
        return context


class ShowPost(DetailView):
    model = Menu
    template_name = 'menu/post.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['post']
        return context


class Login(LoginView):
    template_name = 'menu/oauth.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Авторизация'
        return context


def logout_user(request):
    logout(request)
    return redirect('auth')


# def auth(request):
#     context = {
#         'menu': menu,
#         'title': 'Авторизация'
#     }
#     return render(request, 'menu/oauth.html', context=context)


def legends(request):
    context = {
        'menu': menu,
        'title': 'Легенда'
    }
    return render(request, 'menu/legends.html', context=context)


def contacts(request):
    context = {
        'menu': menu,
        'title': 'Контакты'
    }
    return render(request, 'menu/contacts.html', context=context)


def reviews(request):
    context = {
        'menu': menu,
        'title': 'Отзывы'
    }
    return render(request, 'menu/reviews.html', context=context)


def table_reservation(request):
    context = {
        'menu': menu,
        'title': 'Бронирование столика'
    }
    return render(request, 'menu/table_reservation.html', context=context)








