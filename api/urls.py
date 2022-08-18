import imp
from django.urls import path

from api.views import *

urlpatterns = [
    path('home/', home),
    path('products/', products),
    path('drf/', drf_response)
]
