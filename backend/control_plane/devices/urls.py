from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListAllDevices.as_view(), name='list'),
    path('on_maintenance', views.DevicesOnMaintenance.as_view(), name='on_maintenance'),
    path('update_maintenance_status/<int:id>', views.UpdateDeviceMaintenanceStatus.as_view(), name='update_maintenance_status'),
    path('add', views.AddNewDevice.as_view(), name='add'),
    path('delete/<int:id>', views.DeleteDevice.as_view(), name='delete'),
]