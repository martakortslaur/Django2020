from django.urls import path
from .views import get_second_page
urlpatterns = [
    path('bonjour', get_second_page, name=''),
    
]