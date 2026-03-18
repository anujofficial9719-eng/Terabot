import requests
import re
from login import login_and_get_cookie
from config import TB_EMAIL, TB_PASSWORD

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://www.terabox.com/"
}

# ✅ get cookie
def get_cookie():
    try:
        with open("cookies.txt") as f:
            return {"ndus": f.read().strip().replace("ndus=", "").replace(";", "")}
    except:
        return None

# ✅ ensure login
def ensure_login():
    cookies = get_cookie()
    if not cookies:
        login_and_get_cookie()
        cookies = get_cookie()
    return cookies

# ✅ resolve all types of links
def resolve_url(url):
    try:
        r = requests.get(url, headers=HEADERS, allow_redirects=True, timeout=10)
        return r.url
    except:
        return url

# ✅ extract surl
def extract_surl(url):
    match = re.search(r'/s/([a-zA-Z0-9_-]+)', url)
    return match.group(1) if match else None

# ✅ get files
def get_files(shorturl):
    cookies = ensure_login()

    api = f"https://www.terabox.com/share/list?app_id=250528&shorturl={shorturl}&root=1"

    try:
        res = requests.get(api, headers=HEADERS, cookies=cookies, timeout=15)
        data = res.json()
    except:
        return []

    # 🔁 cookie expired → relogin
    if "errno" in data:
        login_and_get_cookie()
        cookies = get_cookie()

        try:
            res = requests.get(api, headers=HEADERS, cookies=cookies, timeout=15)
            data = res.json()
        except:
            return []

    return data.get("list", [])

# ✅ main extractor
def extract(url):
    try:
        url = resolve_url(url)

        surl = extract_surl(url)
        if not surl:
            return {"status": "error", "msg": "Invalid or unsupported link"}

        files = get_files(surl)

        if not files:
            return {"status": "error", "msg": "No files found"}

        result = []
        for f in files:
            result.append({
                "name": f.get("server_filename"),
                "size": f.get("size"),
                "link": f.get("dlink")
            })

        return {
            "status": "success",
            "count": len(result),
            "files": result
        }

    except Exception as e:
        return {"status": "error", "msg": str(e)}
