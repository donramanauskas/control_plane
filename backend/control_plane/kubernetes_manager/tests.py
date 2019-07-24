from django.test import TestCase
from django.urls import reverse


class KubernetesManagerInfo(TestCase):

    def test_kubernetes_manager_info_view(self):
        url = reverse('kubernetes_manager:info')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
