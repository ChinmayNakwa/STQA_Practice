from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def count_objects():

    driver = None

    try:
        print("===== OBJECT COUNT TEST STARTED =====")
        driver = webdriver.Chrome()
        driver.maximize_window()
        print("Browser launched successfully")

        file_path = os.path.abspath("index.html")
        file_path = file_path.replace("\\", "/")
        driver.get(f"file:///{file_path}")

        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        print("Page loaded successfully")

        elements = driver.find_elements(By.XPATH, "//*")
        total = len(elements)

        print("\nTotal number of objects on page:", total)

        tags = ["div", "p", "span", "a", "button", "input"]

        print("\n--- Object Count by Type ---")
        for tag in tags:
            count = len(driver.find_elements(By.TAG_NAME, tag))
            print(f"{tag.upper()}: {count}")

        time.sleep(2)

        print("\n✓ Test Completed Successfully")

    except Exception as e:
        print("Error occurred:", str(e))

    finally:
        if driver:
            driver.quit()
            print("Browser closed")


if __name__ == "__main__":
    count_objects()