from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from menu.models import Menu, Category
from menu.serializers import CategorySerializer


class CategoryTestCase(APITestCase):
    def test_get(self):
        category_1 = Category.objects.create(name='meat')
        category_2 = Category.objects.create(name='pechka')
        ab = category_2
        ac = category_1
        url = reverse('category-list')
        response = self.client.get(url)
        serializer_data = CategorySerializer([category_1, category_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)


# class MenuTestCase(APITestCase, CategoryTestCase):
#     def test_get(self):
#         menu_1 = Menu.objects.create(name='hinkali', description='qwerty', photo='qwerty', price=390, rating=4.8,
#                                      weight=390, category=category_1)
#         menu_2 = Menu.objects.create(name='hachapuri', description='qwerty', photo='qwerty', price=490, rating=4.8,
#                                      weight=500, category=category_2)
#         url = reverse('menu-list')
#         response = self.client.get(url)
#         serializer_data = CategorySerializer([menu_1, menu_2], many=True).data
#         self.assertEqual(status.HTTP_200_OK, response.status_code)
#         self.assertEqual(serializer_data, response.data)


