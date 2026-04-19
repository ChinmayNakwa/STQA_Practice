from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def count_list_items():

    driver = None

    try:
        print("===== LIST COUNT TEST STARTED =====")

        driver = webdriver.Chrome()
        driver.maximize_window()

        file_path = os.path.abspath("index.html")
        file_path = file_path.replace("\\", "/")
        driver.get(f"file:///{file_path}")

        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        print("Page loaded successfully")

        lists = driver.find_elements(By.TAG_NAME, "ul")
        print("\nTotal lists:", len(lists))
        
        for i, ul in enumerate(lists, 1):
            items = ul.find_elements(By.TAG_NAME, "li")
            print(f"\nList {i} items: {len(items)}")

            for j, item in enumerate(items, 1):
                print(f"  {j}. {item.text}")

        dropdowns = driver.find_elements(By.TAG_NAME, "select")
        print("\nTotal dropdowns:", len(dropdowns))

        for i, dropdown in enumerate(dropdowns, 1):
            options = dropdown.find_elements(By.TAG_NAME, "option")
            print(f"\nDropdown {i} options: {len(options)}")

            for j, opt in enumerate(options, 1):
                print(f"  {j}. {opt.text}")

        time.sleep(2)

        print("\n✓ Test Completed Successfully")

    except Exception as e:
        print("Error:", str(e))

    finally:
        if driver:
            driver.quit()
            print("Browser closed")


if __name__ == "__main__":
    count_list_items()