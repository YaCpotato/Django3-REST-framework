# coding: utf-8

from rest_framework import routers
from .views import ProductViewSet,ClientViewSet,OrderViewSet
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('csv', views.csv_import, name='csv')
]

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'orders',OrderViewSet)