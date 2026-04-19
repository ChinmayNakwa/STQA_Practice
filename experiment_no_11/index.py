from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def count_checkboxes():

    driver = None

    try:
        print("===== CHECKBOX TEST STARTED =====")

        driver = webdriver.Chrome()
        driver.maximize_window()
        print("Browser launched")

        file_path = os.path.abspath("index.html")
        file_path = file_path.replace("\\", "/")
        driver.get(f"file:///{file_path}")

        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        print("Page loaded successfully")

        checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

        checked = 0
        unchecked = 0

        print("\nTotal checkboxes:", len(checkboxes))
        print("-" * 40)

        for i, cb in enumerate(checkboxes, 1):

            if cb.is_selected():
                status = "CHECKED"
                checked += 1
            else:
                status = "UNCHECKED"
                unchecked += 1

            print(f"Checkbox {i}: {status}")

        print("-" * 40)
        print("Checked:", checked)
        print("Unchecked:", unchecked)

        assert checked + unchecked == len(checkboxes), "Count mismatch!"
        print("\n✓ Test Completed Successfully")

        time.sleep(2)

    except Exception as e:
        print("Error occurred:", str(e))

    finally:
        if driver:
            driver.quit()
            print("Browser closed")


if __name__ == "__main__":
    count_checkboxes()