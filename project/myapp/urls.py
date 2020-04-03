# coding: utf-8

from rest_framework import routers
from .views import ProductViewSet,ClientViewSet,OrderViewSet


router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'orders',OrderViewSet)