from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('auth/', auth, name='auth'),
    path('legends/', legends, name='legends'),
    path('', MenuHome.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('reviews/', reviews, name='reviews'),
    path('table_reservation/', table_reservation, name='table_reservation'),
    path('post/<int:post_id>/', ShowPost.as_view(), name='post'),
    path('category/<int:category_id>/', ShowCategory.as_view(), name='category'),
    ]
