import csv
from kubernetes import client, config

def get_containers_running_as_root(api_instance, namespace="default"):
    containers_running_as_root = []

    # List all pods in the specified namespace
    pods = api_instance.list_namespaced_pod(namespace, watch=False)

    # Iterate through each pod
    for pod in pods.items:
        # Iterate through each container in the pod
        for container in pod.spec.containers:
            # Check if the container is running as root
            if container.security_context and container.security_context.run_as_user == 0:
                containers_running_as_root.append({
                    "Namespace": pod.metadata.namespace,
                    "Pod": pod.metadata.name,
                    "Container": container.name
                })

    return containers_running_as_root

def get_nodes_running_as_root(api_instance):
    nodes_running_as_root = []

    # List all nodes in the cluster
    nodes = api_instance.list_node(watch=False)

    # Iterate through each node
    for node in nodes.items:
        # Check if the node is running as root
        if node.spec and node.spec.operating_system == "linux" and node.spec.user == "root":
            nodes_running_as_root.append({
                "Node": node.metadata.name
            })

    return nodes_running_as_root

def generate_csv_report(data, csv_filename):
    keys = data[0].keys() if data else []
    with open(csv_filename, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

def main():
    # Prompt user for Kubernetes configuration file path
    kubeconfig_path = input("Enter the path to your Kubernetes configuration file (default: ~/.kube/config): ").strip() or "~/.kube/config"

    # Prompt user for namespace
    namespace = input("Enter the namespace to search for containers (default: default): ").strip() or "default"

    # Load the Kubernetes configuration
    config.load_kube_config(kubeconfig_path)

    # Create a Kubernetes API client
    api_instance = client.CoreV1Api()

    # Get containers running as root
    containers_running_as_root = get_containers_running_as_root(api_instance, namespace)

    # Get nodes running as root
    nodes_running_as_root = get_nodes_running_as_root(api_instance)

    # Combine container and node data
    all_resources_running_as_root = containers_running_as_root + nodes_running_as_root

    # Generate CSV report
    generate_csv_report(all_resources_running_as_root, "root_resources_report.csv")

    print("CSV report generated successfully.")

if __name__ == "__main__":
    main()
