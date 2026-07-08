from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    autho = models.CharField(max_length=50)
    isbn = models.CharField(max_length=10)
    pubdate = models.DateField()
    pricestandard = models.IntegerField()
    adult = models.BooleanField()
    salespoint = models.IntegerField()
    publisher = models.CharField(max_length=50)