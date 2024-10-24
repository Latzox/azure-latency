from flask import Flask, render_template, request, jsonify
from latency_test import test_latency, endpoints
from check_endpoint_health import check_endpoints_health  # Import the health check function
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test-latency', methods=['GET'])
def latency():
    results = {}
    for region, urls in endpoints.items():
        latency_result = test_latency(urls["latency_url"])  # Pass the latency URL to test_latency()
        if latency_result is not None:
            results[region] = f"{latency_result:.2f} ms"
        else:
            results[region] = "Failed to measure latency"
    return jsonify(results)

# New route to return all available endpoints
@app.route('/endpoints', methods=['GET'])
def get_endpoints():
    return jsonify(endpoints)

# New route to check health status of endpoints
@app.route('/check-health', methods=['GET'])
def check_health():
    health_results = check_endpoints_health()
    return jsonify(health_results)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
