from flask import Flask, render_template
from latency_test import test_latency

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test-latency')
def latency():
    result = test_latency()
    return f'Latency results: {result}'

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0', port=80)
