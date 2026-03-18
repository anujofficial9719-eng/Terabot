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
        login_and_get_cookie(TB_EMAIL, TB_PASSWORD)
        cookies = get_cookie()
    return cookies

# ✅ resolve all types of links
def resolve_url(url):
    try:
        r = requests.get(url, headers=HEADERS, allow_redirects=True, timeout=10)
        return r.url
    except:
        return url
