from rest_framework.serializers import ModelSerializer

from menu.models import Menu, Category


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'name', 'description', 'price', 'rating', 'weight', 'category')


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'