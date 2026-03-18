from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

from config import TB_EMAIL, TB_PASSWORD

def login_and_get_cookie():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # VPS ke liye
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    try:
        driver.get("https://www.terabox.com/")

        time.sleep(5)

        # 👉 Login button click
        driver.find_element(By.XPATH, "//a[contains(@class,'login')]").click()
        time.sleep(3)

        # 👉 Email input
        driver.find_element(By.NAME, "username").send_keys(TB_EMAIL)

        # 👉 Password input
        driver.find_element(By.NAME, "password").send_keys(TB_PASSWORD)
        driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)

        time.sleep(8)

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
