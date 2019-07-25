from django.test import TestCase
from django.urls import reverse

from unittest.mock import patch


class KubernetesManagerInfoViewTests(TestCase):

    def test_kubernetes_manager_info_view(self):
        url = reverse('kubernetes_manager:info')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class KubernetesPodsInfoViewTests(TestCase):

    @patch('business_logic.kubernetes.kubernetes_interface.KubernetesInterface.info',
           return_value=[{'172.17.0.3': {'kube-system': 'coredns-5c98db65d4-2s58n'}}])
    def test_kubernetes_pod_info_view(self, mock_kubernetes_api_call):
        """
        Test get Kubernetes POD info view.
        API call to external Kubernetes api mocked by mock_kubernetes_api_call
        """

        url = reverse('kubernetes_manager:pod_info')
        response = self.client.get(url)
        print(response.data)
