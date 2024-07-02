from django.urls import path
from .views import *

urlpatterns = [
    path('Login/', Login, name='Login'),
    path('Home/', Home, name='Home'),
    path('ThemNguoiDung/', ThemNguoiDung, name='ThemNguoiDung'),
]