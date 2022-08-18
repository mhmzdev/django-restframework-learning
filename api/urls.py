import imp
from django.urls import path

from api.views import *

urlpatterns = [
    path('', home),
    path('product/', products),
    path('drf/', drf_response)
]
