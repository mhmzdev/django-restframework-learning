from django.urls import path

from .views import home
from .views import products

urlpatterns = [
    path('', home),
    path('product/', products)
]