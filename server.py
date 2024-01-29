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

    pubmed = PubMed(tool="YourToolName", email="YourEmail@example.com")
    search_results = pubmed.query(query, max_results=max_results)

    articles = []
    for article in search_results:
        articles.append({
            "title": article.title,
            "abstract": article.abstract,
            "publication_date": str(article.publication_date),
            "authors": [author['lastname'] + ' ' + author['initials'] for author                                                                                                                                    in article.authors],
            "doi": article.doi,
            "pmid": article.pubmed_id
        })

    return jsonify(articles)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
