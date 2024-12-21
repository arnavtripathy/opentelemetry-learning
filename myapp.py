#docker command - docker run -d -p 4317:4317 -p 16686:16686 --name jaeger jaegertracing/all-in-one:latest
from flask import Flask, request, jsonify
import requests
import time

# Create a Flask app
app = Flask(__name__)

@app.route("/")
def home():
    # Simulate processing time
    time.sleep(0.5)
    return jsonify({"message": "Welcome to the Zero-Code Instrumentation Demo!"})

@app.route("/api", methods=["GET"])
def api_call():
    # Simulate an external HTTP call
    response = requests.get("https://httpbin.org/get")
    return jsonify({
        "message": "Fetched data from an external API",
        "data": response.json()
    })

@app.route("/process", methods=["POST"])
def process_data():
    # Simulate processing some data
    data = request.json
    time.sleep(1)
    return jsonify({"message": "Processed your data", "input": data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)