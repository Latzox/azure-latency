import requests
import time
import json
import os

# Load endpoint configuration
config_file_path = os.path.join(os.path.dirname(__file__), 'endpoints.json')
with open(config_file_path) as config_file:
    endpoints = json.load(config_file)

def get_latency(url):
    try:
        start_time = time.time()
        response = requests.get(url, timeout=5)  # Set timeout to 5 seconds
        end_time = time.time()

        if response.status_code == 200:
            return (end_time - start_time) * 1000  # latency in milliseconds
        else:
            return None
    except requests.RequestException as e:
        print(f"Error connecting to {url}: {e}")
        return None

def test_latency(url=None):
    if url:
        # If a specific URL is provided, only test that URL
        return get_latency(url)
    else:
        # If no URL is provided, test all endpoints
        return test_latency_all()

def test_latency_all():
    results = {}
    for region, urls in endpoints.items():
        latency = get_latency(urls["latency_url"])  # Use latency_url for latency check
        if latency is not None:
            results[region] = f"{latency:.2f} ms"
        else:
            results[region] = "Failed to measure latency"
    return results

if __name__ == "__main__":
    results = test_latency_all()
    for region, latency in results.items():
        print(f"Latency to {region}: {latency}")
