from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from menu.models import Menu, Category
from menu.serializers import CategorySerializer, MenuSerializer


class CategoryTestCase(APITestCase):
    def setUp(self):
        self.category_1 = Category.objects.create(name='Напитки')
        self.category_2 = Category.objects.create(name='Блюда из печи')

    def test_get(self):
        url = reverse('category-list')
        response = self.client.get(url)
        serializer_data = CategorySerializer([self.category_1, self.category_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
        print(serializer_data, response.data)


class MenuTestCase(APITestCase):
    def setUp(self):
        self.menu_1 = Menu.objects.create(name='Компот Айва 250мл', description='компот из айвы',
                                     photo='qwerty', price=390, rating=4.8,
                                     weight=250, category=Category.objects.create(name='напитки'))
        self.menu_2 = Menu.objects.create(name='хачапури по-мегрельски', description='qwerty',
                                     photo='qwerty', price=390, rating=4.8,
                                     weight=500, category=Category.objects.create(name='блюда из печи'))

    def test_get(self):
        url = reverse('menu-list')
        response = self.client.get(url)
        serializer_data = MenuSerializer([self.menu_1, self.menu_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_filter(self):
        url = reverse('menu-list')
        response = self.client.get(url, data={'price': 390})
        serializer_data = MenuSerializer([self.menu_1, self.menu_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
