from django.urls import path

from . import views

urlpatterns = [
    path('add', views.AddNewDevice.as_view(), name='add')
]