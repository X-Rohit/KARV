#from inspect import _SourceObjectType
#from socketserver import StreamRequestHandler
#from unicodedata import category
from django.db import models


class register(models.Model):
    username=models.CharField(max_length=50,primary_key=True)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    coins=models.CharField(max_length=5)


class Secret(models.Model):

    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    sector=models.CharField( max_length=50)
    symbol=models.CharField(max_length=5)
    price=models.CharField(max_length=10)
    peratio=models.CharField(max_length=10)
    weekup=models.CharField(max_length=10)
    weekdown=models.CharField(max_length=10)

class Transaction(models.Model):

    username=models.CharField(max_length=50)
    ticker=models.CharField(max_length=50)
    TotalShare=models.CharField(max_length=5)
    TotalAmount=models.CharField(max_length=5)
    status=models.CharField(max_length=10)

