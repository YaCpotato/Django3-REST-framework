# coding: utf-8

import django_filters
from rest_framework import viewsets, filters
from django.shortcuts import render,redirect

from .models import Product,Client,Order
from .serializer import ProductSerializer, ClientSerializer, OrderSerializer
from io import TextIOWrapper
import csv,re

def index(request):
    return render(request, 'index.html')

def csv_import(request):
    if 'csv' in request.FILES:
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_file = csv.reader(form_data)
        
        result = re.match('(.*)(?=\.)',request.FILES['csv'].name)
        print(result.group())
        # ヘッダーでバリデーションを行う時に使う... return ['ヘッダー1','ヘッダー2',...]
        next(csv_file)

        for line in csv_file:
            product = Product(
                number = line[0],
                name = line[1],
                price = line[2]
            )
        
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
