from django.urls import path

from .views import KubernetesInfoView

urlpatterns = [
    path('info/', KubernetesInfoView.as_view(), name='info')
]