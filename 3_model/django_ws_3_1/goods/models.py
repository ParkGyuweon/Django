from django.db import models

# Create your models here.
class goods_product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    is_published = models.BooleanField()