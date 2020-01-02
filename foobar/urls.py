from django.urls import path
from .views import get_first_page, get_2020_page
urlpatterns = [
    path('hello', get_first_page, name=''),
    path('year-2020', get_2020_page, name='')
]