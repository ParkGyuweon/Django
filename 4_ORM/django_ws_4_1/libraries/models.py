from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.IntegerField()
    author = models.CharField(max_length=50)
    pubdate = models.DateField()
    price = models.IntegerField()
    adult = models.BooleanField()