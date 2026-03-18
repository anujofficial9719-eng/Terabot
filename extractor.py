import requests
import re
from login import login_and_get_cookie   # 👈 added

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

# ✅ resolve short link
def resolve_url(url):
    r = requests.get(url, allow_redirects=True)
    return r.url

# ✅ extract surl
def extract_surl(url):
    match = re.search(r'/s/([a-zA-Z0-9_-]+)', url)
    return match.group(1) if match else None

# ✅ get files with auto login
def get_files(shorturl):
    cookies = get_cookie()

    # 🔁 agar cookie nahi hai → login
    if not cookies:
        login_and_get_cookie()
        cookies = get_cookie()

    api = f"https://www.terabox.com/share/list?app_id=250528&shorturl={shorturl}&root=1"

    res = requests.get(api, headers=HEADERS, cookies=cookies)
    data = res.json()

    # 🔁 agar cookie expire ho gaya
    if "errno" in data:
        login_and_get_cookie()
        cookies = get_cookie()

        res = requests.get(api, headers=HEADERS, cookies=cookies)
        data = res.json()

    return data.get("list", [])

# ✅ main extract function
def extract(url):
    try:
        url = resolve_url(url)

        surl = extract_surl(url)
        if not surl:
            return {"status": "error", "msg": "Invalid link"}

        files = get_files(surl)

        result = []
        for f in files:
            result.append({
                "name": f["server_filename"],
                "size": f["size"],
                "link": f["dlink"]
            })

        return {"status": "success", "files": result}

    except Exception as e:
        return {"status": "error", "msg": str(e)}
