from kubernetes import client, config


class KubernetesInterface:

    def __init__(self):
        config.load_kube_config()
        self.v1 = client.CoreV1Api()

    def info(self):
        ret = self.v1.list_pod_for_all_namespaces(watch=False)
        pods = []
        for i in ret.items:
            pods.append({i.status.pod_ip: {i.metadata.namespace: i.metadata.name}})
        return pods
