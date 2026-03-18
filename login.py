import os

def login_and_get_cookie(email=None, password=None):
    """
    ⚠️ Direct login unreliable hai
    Isliye manual cookie system use karo
    """

    if os.path.exists("cookies.txt"):
        print("✅ Using existing cookie")
        return True

    print("❌ No cookie found!")
    print("👉 Manually add cookie in cookies.txt like:")
    print("ndus=YOUR_COOKIE_HERE;")

    return False
