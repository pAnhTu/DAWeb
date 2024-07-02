# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('Add_Department/', Add_Department.as_view(), name='Add_Department'),
    # Các đường dẫn khác...
]