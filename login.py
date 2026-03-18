import requests
from config import TB_EMAIL, TB_PASSWORD

def login_and_get_cookie():
    session = requests.Session()

    url = "https://passport.terabox.com/v2/api/?login"

    data = {
        "username": TB_EMAIL,
        "password": TB_PASSWORD
    }

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    res = session.post(url, data=data, headers=headers)

    cookies = session.cookies.get_dict()

    if "ndus" in cookies:
        with open("cookies.txt", "w") as f:
            f.write(f"ndus={cookies['ndus']};")

        print("✅ Cookie generated")
        return True

    print("❌ Login failed")
    return False
