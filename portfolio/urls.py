from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('pro1', views.pro1, name='pro1'),
    path('pro2', views.pro2, name='pro2'),
    path('pro3', views.pro3, name='pro3'),
]
