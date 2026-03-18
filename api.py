from flask import Flask, request, jsonify
from extractor import extract

app = Flask(__name__)

@app.route("/api")
def api():
    url = request.args.get("url")
    return jsonify(extract(url))

app.run(host="0.0.0.0", port=5000)
