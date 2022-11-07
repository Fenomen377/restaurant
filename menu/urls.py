from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('auth/', auth, name='auth'),
    path('legends/', legends, name='legends'),
    path('', index, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('reviews/', reviews, name='reviews'),
    path('table_reservation/', table_reservation, name='table_reservation'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('category/<int:category_id>/', show_category, name='category'),
    ]