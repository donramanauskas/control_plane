from django.urls import path

from . import views

urlpatterns = [
    path('info/', views.KubernetesInfoView.as_view(), name='info'),
    path('pod_info/', views.KubernetesPodInfo.as_view(), name='pod_info')
]