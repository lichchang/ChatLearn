from flask import Flask, request, jsonify
from pymed import PubMed
import json

app = Flask(__name__)

@app.route('/fetch_papers', methods=['POST'])
def fetch_papers():
    # Ensure JSON in request
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400

    data = request.get_json()
    query = data.get('query', '')
    max_results = data.get('max_results', 10)

    # Validate query
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400
from flask import Flask, request, jsonify
