# AWS EKS Root Resources Finder

## Overview

This Python tool is designed to find and generate a CSV report of resources running as root in an AWS EKS environment. It utilizes the Kubernetes Python client library to query information about containers and nodes within the specified Kubernetes cluster.

## Prerequisites

- Python 3.x
- `kubernetes` Python library (`pip install kubernetes`)

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/Parthasarathi7722/find_R00T.git
    ```

2. Navigate to the project directory:

    ```bash
    cd eks-root-resources-finder
    ```

3. Run the script:

    ```bash
    python eks_root_resources_finder.py
    ```

4. Follow the prompts to provide the necessary inputs, such as Kubernetes configuration and namespace.

5. Once the script completes, a CSV report named `root_resources_report.csv` will be generated in the project directory.

## Script Details

The `eks_root_resources_finder.py` script performs the following:

- Prompts the user for Kubernetes configuration file path.
- Prompts the user for the namespace (default is `default`).
- Queries information about containers running as root in the specified namespace.
- Queries information about nodes running as root in the entire cluster.
- Combines the data and generates a CSV report.

Feel free to customize the script or extend its functionality based on your specific requirements.

