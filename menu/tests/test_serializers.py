from unittest import TestCase

from menu.models import Menu, Category
from menu.serializers import MenuSerializer, CategorySerializer


class MenuSerializerTestCase(TestCase):
    def test_ok(self):
        menu_1 = Menu.objects.create(name='Компот', description='компот',
                                     price=390, rating=4.8,
                                     weight=250, category=Category.objects.create(name='напитки'))
        menu_2 = Menu.objects.create(name='хачапури по-мегрельски', description='qwerty',
                                     price=490, rating=4.8,
                                     weight=500, category=Category.objects.create(name='блюда из печи'))
        data = MenuSerializer([menu_1, menu_2], many=True).data
        expected_data = [
            {
                'id': menu_1.id,
                'name': 'Компот',
                'description': 'компот',
                'price': '390.00',
                'rating': '4.80',
                'weight': '250.00',
                'category': menu_1.category_id
            },
            {
                'id': menu_2.id,
                'name': 'хачапури по-мегрельски',
                'description': 'qwerty',
                'price': '490.00',
                'rating': '4.80',
                'weight': '500.00',
                'category': menu_2.category_id
            }
        ]
        self.assertEqual(data, expected_data)
        print(data, expected_data)


class CategorySerializerTestCase(TestCase):
    def test_ok(self):
        category_1 = Category.objects.create(name='Напитки')
        category_2 = Category.objects.create(name='Блюда из печи')
        data = CategorySerializer([category_1, category_2], many=True).data
        expected_data = [
            {
                'id': category_1.id,
                'name': 'Напитки'
            },
            {
                'id': category_2.id,
                'name': 'Блюда из печи'
            }
        ]
        self.assertEqual(data, expected_data)
        print(data, expected_data)
