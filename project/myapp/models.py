from django.db import models

# Create your models here.
class Product(models.Model):
    number = models.CharField(verbose_name='商品番号',max_length=10,primary_key=True)
    name = models.CharField(verbose_name='商品名',max_length=200)
    price = models.IntegerField(verbose_name='価格')

class Client(models.Model):
    number = models.CharField(verbose_name='顧客番号',max_length=10,primary_key=True)
    name = models.CharField(verbose_name='顧客名',max_length=200)
    adress = models.TextField(
        verbose_name='住所',
        max_length=1000
    )


class Order(models.Model):
    number = models.CharField(verbose_name='注文番号',max_length=10,primary_key=True)
    client_number = models.ForeignKey(
        'Client',
        verbose_name='顧客',
        on_delete=models.CASCADE
    )
    product_number = models.ForeignKey(
        'Product',
        verbose_name='商品',
        on_delete=models.CASCADE
    )
    quantity = models.CharField(verbose_name='数量',max_length=200)
