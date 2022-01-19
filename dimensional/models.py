from operator import mod
from pyexpat import model
from re import L
from django.db import models
import dimensionaltech.settings as settings

# Create your models here.

class dest(models.Model):
    file = models.FileField(upload_to='static/upload')

class data(models.Model):
    image_name = models.CharField(max_length=150)
    object_detected = models.CharField(max_length=300)
    timestamp = models.DateField()


def handle_uploaded_file(f):
    print(f)
    with open('static/upload/'+ f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
