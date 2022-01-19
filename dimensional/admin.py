import imp
from django.contrib import admin
from .models import dest, data

admin.site.register(dest)
admin.site.register(data)

# Register your models here.
