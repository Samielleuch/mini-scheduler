from kubernetes import client, config
from kubernetes.client.rest import ApiException
# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config("./config")
queue = [
    {"name": "challenge1", "image": "nginx"},
    {"name": "challenge2", "image": "nginx"}
]

v1 = client.CoreV1Api()
print("Provisioning Challenges :")

for item in queue:
    resp = None
    try:
        resp = v1.read_namespaced_pod(name=item.get("name"),
                                                namespace='default')
    except ApiException as e:
        if e.status != 404:
            print("Unknown error: %s" % e)
            exit(1)
    if not resp:
        print("YOO")
        print("Pod %s does not exist. Creating it..." % item.get("name"))
        pod_manifest = {
            'apiVersion': 'v1',
            'kind': 'Pod',
            'metadata': {
                'name': item.get("name")
            },
            'spec': {
                'containers': [{
                    'image': item.get("image"),
                    'name': item.get("name")
                }]
            }
        }
        resp = v1.create_namespaced_pod(body=pod_manifest, namespace='default')
