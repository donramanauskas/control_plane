from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from business_logic.kubernetes.kubernetes_interface import KubernetesInterface


class KubernetesInfoView(APIView):

    def get(self, request):
        return Response("Welcome to Kubernetes Manager", status.HTTP_200_OK)


class KubernetesPodInfo(APIView):

    def get(self, request):
        try:
            k = KubernetesInterface()
            pod_info_dict = k.info()
            return Response(pod_info_dict, status.HTTP_200_OK)
        except:
            return Response(status.HTTP_400_BAD_REQUEST, "Failed to get PODs from Kubernetes Master")
