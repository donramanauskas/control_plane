from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListAllDevices.as_view(), name='list'),
    path('add', views.AddNewDevice.as_view(), name='add')
]