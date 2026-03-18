from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

from config import TB_EMAIL, TB_PASSWORD


def login_and_get_cookie():
    options = webdriver.ChromeOptions()

    # 🔥 VPS optimized
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    try:
        print("🔐 Opening TeraBox...")

        driver.get("https://www.terabox.com/")
        time.sleep(5)

        # 🔘 Login button (safe click)
        try:
            driver.find_element(By.XPATH, "//a[contains(@class,'login')]").click()
        except:
            pass

        time.sleep(3)

        print("✉️ Entering credentials...")

        # 📧 Email
        driver.find_element(By.NAME, "username").send_keys(TB_EMAIL)

        # 🔑 Password
        password_box = driver.find_element(By.NAME, "password")
        password_box.send_keys(TB_PASSWORD)
        password_box.send_keys(Keys.RETURN)

        time.sleep(10)

        print("🍪 Fetching cookies...")

        cookies = driver.get_cookies()

        for cookie in cookies:
            if cookie['name'] == "ndus":
                with open("cookies.txt", "w") as f:
                    f.write(f"ndus={cookie['value']};")

                print("✅ Cookie generated successfully")
                driver.quit()
                return True

        print("❌ ndus cookie not found")
        driver.quit()
        return False

    except Exception as e:
        print("❌ Login Error:", e)
        driver.quit()
        return False
