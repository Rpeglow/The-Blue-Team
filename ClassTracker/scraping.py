import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from chromedriver_py import binary_path

def scrape_course_data(class_number):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--silent')
    chrome_options.add_argument('--disable-logging')

    svc = webdriver.ChromeService(executable_path=binary_path)
    driver = webdriver.Chrome(service=svc, options=chrome_options)

    try:
        driver.get('https://catalog.ivytech.edu')

        class_input = driver.find_element(By.ID, 'keyword')
        class_input.send_keys(class_number)

        search_button = driver.find_element(By.ID, 'keyword-submit-icon')
        search_button.click()

        try:
            best_match_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(.,'Best Match:')]"))
            )
            best_match_element.click()

            course_heading_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".coursepadding h3"))
            )

            course_heading_text = course_heading_element.text.strip()
            course_number, course_name = map(str.strip, course_heading_text.split('-', 1))

            course_text_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".coursepadding > div:nth-child(2)"))
            )

            course_text = course_text_element.text.strip()

            description_pattern = r'DATE OF LAST REVISION:.+\s\s(?P<description>.*)\s\sMAJOR COURSE LEARNING OBJECTIVES'

            match = re.search(description_pattern, course_text, re.DOTALL)
            if match:
                course_description = match.group('description').strip()
            else:
                course_description = "Not found"

            return course_number, course_name, course_description

        except Exception as e:
            print("Best Match element not found:", e)
            return None

    finally:
        driver.quit()
