from django.urls import path

from . import views

urlpatterns = [
    path('zabbix_hosts/', views.GetZabbixMonitoredHosts.as_view(), name='zabbix_hosts')
]