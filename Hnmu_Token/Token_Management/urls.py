from django.urls import path
from .views import *
urlpatterns = [
    path('check_token/', CheckTokenAPIView.as_view(), name='check_token'),
    path('get_token/', TokenView.as_view(), name='get_token'),
]