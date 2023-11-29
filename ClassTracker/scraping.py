import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException

def find_element_with_retry(driver, by, value, timeout=20, retries=3):
    attempts = 0
    while attempts < retries:
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return element
        except TimeoutException:
            print(f"Element not found. Retrying... Attempt {attempts + 1}/{retries}")
            attempts += 1
    print(f"Element not found after {retries} retries.")
    return None

def scrape_course_data(class_number):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get('https://catalog.ivytech.edu')

        class_input = driver.find_element(By.ID, 'keyword')
        class_input.send_keys(class_number)

        search_button = driver.find_element(By.ID, 'keyword-submit-icon')
        search_button.click()

        try:
            best_match_element = find_element_with_retry(driver, By.XPATH, "//a[contains(.,'Best Match:')]")
            if best_match_element:
                print('Found best match link')

            main_window = driver.current_window_handle
            best_match_element.click()
            time.sleep(10)
            all_windows = driver.window_handles

            if len(all_windows) > 1:
                print('Starting popup window logic...')
                for window in all_windows:
                    if window != main_window:
                        driver.switch_to.window(window)
                        course_heading_element = find_element_with_retry(driver, By.CSS_SELECTOR, ".toplevel_popup h1")
                        if course_heading_element:
                            print('Found h1 element')
                        
                        course_heading_text = course_heading_element.text.strip()
                        course_number, course_name = map(
                            str.strip, course_heading_text.split('-', 1))

                        course_text_element = find_element_with_retry(driver, By.CSS_SELECTOR, ".block_content_popup")
                        if course_text_element:
                            print('Found popup content block')

                        course_text = course_text_element.text.strip()

                        description_pattern = r'DATE OF LAST REVISION:.+\s\s(?P<description>.*)\s\sMAJOR COURSE LEARNING OBJECTIVES'

                        match = re.search(description_pattern,
                                          course_text, re.DOTALL)
                        if match:
                            course_description = match.group(
                                'description').strip()
                        else:
                            course_description = "Not found"

                        driver.close()
                        driver.switch_to.window(main_window)
                        break
            else:
                print('Starting main window logic...')

                course_heading_element = find_element_with_retry(driver, By.XPATH, "//td/div[2]/h3")
                if course_heading_element:
                    print('Found h3 element')

                course_heading_text = course_heading_element.text.strip()
                course_number, course_name = map(
                    str.strip, course_heading_text.split('-', 1))

                course_text_element = find_element_with_retry(driver, By.XPATH, "//table[2]/tbody/tr[3]/td/table/tbody/tr/td/div[2]")
                if course_text_element:
                    print('Found content block')

                course_text = course_text_element.text.strip()

                description_pattern = r'DATE OF LAST REVISION:.+\s\s(?P<description>.*)\s\sMAJOR COURSE LEARNING OBJECTIVES'

                match = re.search(description_pattern, course_text, re.DOTALL)
                if match:
                    course_description = match.group('description').strip()
                else:
                    course_description = "Not found"

            print(course_number)
            print(course_name)
            print(course_description)

            return course_number, course_name, course_description

        except Exception as e:
            print("Error encountered while scraping:", e)
            return None

    finally:
        driver.quit()