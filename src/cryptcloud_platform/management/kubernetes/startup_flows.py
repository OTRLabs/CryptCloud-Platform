from __future__ import annotations

from pick import pick
from kubernetes import client, config, watch
from datetime import datetime
from kubernetes.client import configuration


def launch_kubernetes_cluster() -> bool:
    """
    Launches a Kubernetes cluster by creating a new cluster.

    This function uses the kubernetes library for python to create a new cluster.
    Returns:
        Boolean: True if the cluster was successfully launched, False otherwise.
    """

    # Load the default configuration
    config.load_kube_config()

    # Create an instance of the API client
    api_client = client.ApiClient()

    # Create an instance of the V1Cluster class
    cluster = client.V1Cluster(
        metadata=client.V1ObjectMeta(name="new-cluster"),
        spec=client.V1ClusterSpec(
            cluster_api_version="v1",
            cluster_ip_range="10.244.0.0/16",
            enable_cloud_provider=True,
            network="flannel",
            service_network="10.96.0.0/12",
            provider_config=client.V1ProviderConfig(
                value="{\"network\":\"10.200.0.0/16\",\"subnetwork\":\"test-subnetwork\"}"
            ),
        ),
    )

    # Create a new cluster
    api_instance = client.CoreV1Api(api_client)
    try:
        api_response = api_instance.create_cluster(cluster)
        print(api_response)
        return True
    except client.rest.ApiException as e:
        print("Exception when calling CoreV1Api->create_cluster: %s\n" % e)
        return False

