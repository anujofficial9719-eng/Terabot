import requests
import re
from flask import Flask, request, jsonify

app = Flask(__name__)

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://www.terabox.com/"
}

def get_cookie():
    with open("cookies.txt") as f:
        return {"ndus": f.read().strip().replace("ndus=", "").replace(";", "")}

def extract(link):
    try:
        cookies = get_cookie()

        html = requests.get(link, headers=HEADERS, cookies=cookies).text

        surl = re.search(r'surl=([a-zA-Z0-9_-]+)', link)
        if not surl:
            return {"status": "error"}

        surl = surl.group(1)

        api = f"https://www.terabox.com/share/list?app_id=250528&shorturl={surl}&root=1"

        data = requests.get(api, headers=HEADERS, cookies=cookies).json()

        file = data["list"][0]

        return {
            "status": "success",
            "filename": file["server_filename"],
            "size": str(file["size"]),
            "download": file["dlink"]
        }

    except Exception as e:
        return {"status": "error", "msg": str(e)}

@app.route("/api")
def api():
    url = request.args.get("url")
    return jsonify(extract(url))

app.run(host="0.0.0.0", port=5000)
