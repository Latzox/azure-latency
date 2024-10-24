import requests
import json
import os

# Load endpoint configuration from endpoints.json
config_file_path = os.path.join(os.path.dirname(__file__), 'endpoints.json')
with open(config_file_path) as config_file:
    endpoints = json.load(config_file)

def get_health_status(health_url):
    try:
        response = requests.get(health_url, timeout=5)  # Set timeout to 5 seconds
        if response.status_code == 200:
            return "Healthy"
        else:
            return "Unhealthy"
    except requests.RequestException as e:
        print(f"Error connecting to {health_url}: {e}")
        return "Unreachable"

def check_endpoints_health():
    health_statuses = {}
    for region, urls in endpoints.items():
        health_status = get_health_status(urls["health_url"])
        health_statuses[region] = health_status
    return health_statuses

if __name__ == "__main__":
    health_results = check_endpoints_health()
    for region, status in health_results.items():
        print(f"Health status of {region}: {status}")
