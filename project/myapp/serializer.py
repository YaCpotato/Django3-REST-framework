# coding: utf-8

from rest_framework import serializers

from .models import Product,Client,Order


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('number', 'name', 'price')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('number', 'name', 'adress')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('number', 'client_number', 'product_number', 'quantity')