from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from menu.models import Menu, Category
from menu.serializers import CategorySerializer, MenuSerializer


class CategoryTestCase(APITestCase):
    def test_get(self):
        category_1 = Category.objects.create(name='Напитки')
        category_2 = Category.objects.create(name='Блюда из печи')
        url = reverse('category-list')
        response = self.client.get(url)
        serializer_data = CategorySerializer([category_1, category_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
        print(serializer_data, response.data)


class MenuTestCase(APITestCase):
    def test_get(self):
        menu_1 = Menu.objects.create(name='Компот Айва 250мл', description='компот из айвы',
                                     photo='qwerty', price=390, rating=4.8,
                                     weight=250, category=Category.objects.create(name='напитки'))
        menu_2 = Menu.objects.create(name='хачапури по-мегрельски', description='qwerty',
                                     photo='qwerty', price=490, rating=4.8,
                                     weight=500, category=Category.objects.create(name='блюда из печи'))
        url = reverse('menu-list')
        response = self.client.get(url)
        serializer_data = MenuSerializer([menu_1, menu_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)



