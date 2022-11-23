from django.db import models


class Item(models.Model):
    name = models.CharField('Название товара', max_length=100)
    description = models.CharField('Описание товара', max_length=100)
    price = models.FloatField('Цена')

