from django.urls import path
from . import views


app_name = 'lotto'

urlpatterns = [
    path('', views.index, name='index'),
]
