from django.urls import path
from .views import get_first_page, get_2020_page, get_ready_page, get_main_page, get_movies, create_movie, update_movie, delete_movie

urlpatterns = [
    path('hello', get_first_page, name=''),
    path('year-2020', get_2020_page, name=''),
    path('get_ready', get_ready_page, name=''),
    path('main_page', get_main_page, name=''),
    path('movies', get_movies, name='get_movies'),
    path('create-movie', create_movie),
    path('update-movie/<pk>', update_movie),
    path('delete-movie/<pk>', delete_movie),
]