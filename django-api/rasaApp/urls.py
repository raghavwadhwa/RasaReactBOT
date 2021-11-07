from rest_framework import routers
from .api import *
from . import api

from django.urls import path

urlpatterns = [
    path('translate/', api.TranslateViewSet.as_view(), name='translate'),
    path('response/', api.ResponseViewSet.as_view(), name='response'),
]
