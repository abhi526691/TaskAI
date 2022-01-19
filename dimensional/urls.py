from django.urls import path
from .views import index, data_show

urlpatterns = [
    path('/', index, name='index'),

]
