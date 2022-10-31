from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(request):
    return HttpResponse('Страница приложения restaurant')


def categories(request, categoryname):
    return HttpResponse(f'<h1>Меню по категориям</h1><p>{categoryname}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')