# coding: utf-8

import django_filters
from rest_framework import viewsets, filters
from django.shortcuts import render,redirect

from .models import Product,Client,Order
from .serializer import ProductSerializer, ClientSerializer, OrderSerializer

def index(request):
    return render(request, 'index.html')

def csv_import(request):
    print('aaaaaaaaaaaaaa')
    return redirect('index')

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
