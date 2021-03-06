"""control_plane URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('get_jwt/', TokenObtainPairView.as_view(), name='get_jwt'),
    path('admin/', admin.site.urls),
    path('devices/', include(('devices.urls', 'devices'), namespace='devices')),
    path('kubernetes_manager/', include(('kubernetes_manager.urls', 'kubernetes_manager'), namespace='kubernetes_manager')),
    path('zabbix/', include(('zabbix_models.urls', 'zabbix'), namespace='zabbix'))
]
