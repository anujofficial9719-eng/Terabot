from flask import Flask, request, jsonify
from extractor import extract

app = Flask(__name__)

@app.route("/api", methods=["GET"])
def api():
    url = request.args.get("url")

    # ❌ agar url nahi mila
    if not url:
        return jsonify({
            "status": "error",
            "msg": "URL parameter missing"
        })

    try:
        return jsonify(extract(url))
    except Exception as e:
        return jsonify({
            "status": "error",
            "msg": str(e)
        })

# 👇 production safe run
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
