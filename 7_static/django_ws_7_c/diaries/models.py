import os
from django.db import models
from django.utils import timezone

# Create your models here.

def diary_image_path(instance, filename):
    dt = timezone.now()
    date_path = dt.strftime('%y/%b/%a')
    return f'diary/{date_path}/{filename}'

class Diary(models.Model):
    content = models.CharField(max_length=125)
    picture = models.ImageField(blank=True, upload_to=diary_image_path)
    created_at = models.DateTimeField(auto_now_add=True)