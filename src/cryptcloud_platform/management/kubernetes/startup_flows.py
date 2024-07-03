from __future__ import annotations

from pick import pick
from kubernetes import client, config, watch
from datetime import datetime
from kubernetes.client import configuration


def launch_kubernetes_cluster() -> None:
    
    print(f"Launching Kubernetes cluster @ {datetime.now()}")