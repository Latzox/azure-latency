import ping3

# Example Azure region endpoints (public IPs for regions or a test server)
AZURE_REGIONS = {
    'East US': '8.8.8.8',
    'West Europe': '8.8.4.4',
    'Southeast Asia': '13.67.67.0',
    # Add more as needed
}

def test_latency():
    results = {}
    for region, ip in AZURE_REGIONS.items():
        latency = ping3.ping(ip)
        results[region] = latency
    return results
