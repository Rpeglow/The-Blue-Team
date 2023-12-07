import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException

def find_element_with_retry(driver, by, value, timeout=20, retries=3):
    """
    Find an element on a web page with retry mechanism.

    Args:
        driver (WebDriver): The WebDriver instance.
        by (str): The locator strategy to use (e.g., "id", "name", "xpath").
        value (str): The value of the locator.
        timeout (int, optional): The maximum time to wait for the element to be found, in seconds. Defaults to 20.
        retries (int, optional): The maximum number of retries. Defaults to 3.

    Returns:
        WebElement or None: The found element, or None if the element is not found after retrying.

    """
    attempts = 0
    # Keep trying to find the element until the maximum number of retries is reached
    while attempts < retries:
        try:
            # Use WebDriverWait to wait for the element to be found
            element = WebDriverWait(driver, timeout, poll_frequency=5, ignored_exceptions=[NoSuchElementException, StaleElementReferenceException]).until(
                EC.presence_of_element_located((by, value))
            )
            return element
        except Exception as e:
            # If the element is not found, refresh the page and try again
            driver.refresh()

            # Wait for the "Best Match:" link to be clickable
            wait = WebDriverWait(driver, 60, poll_frequency=5, ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            best_match_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Best Match:')]")))
            best_match_element.click()
            
            # Wait for the element to be found
            print(f"Element not found. Retrying... Attempt {attempts + 1}/{retries}")
            attempts += 1

    # If the element is not found after retrying, print a message and return None
    if attempts == retries:
        print(f"Reached maximum retries. Element not found after reloading.")
        return None


def scrape_course_data(class_number):
    """
    Scrapes course data from the Ivy Tech catalog website.

    Args:
        class_number (str): The class number to search for.

    Returns:
        tuple: A tuple containing the course number, course name, and course description.
               Returns None if the course data cannot be found.
    """
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--headless') # Run Chrome in headless mode
    chrome_options.add_argument('--disable-gpu') # Needed for Windows
    chrome_options.add_argument('--no-sandbox') # Bypass OS security model
    chrome_options.add_argument('--disable-dev-shm-usage') # Fixes "DevToolsActivePort file doesn't exist" error

    # Create a Chrome WebDriver instance
    driver = webdriver.Chrome(options=chrome_options)
    try:
        # Navigate to the Ivy Tech catalog website
        driver.get('https://catalog.ivytech.edu')

        # Enter the class number into the search box and click the search button
        class_input = driver.find_element(By.ID, 'keyword')
        class_input.send_keys(class_number)

        search_button = driver.find_element(By.ID, 'keyword-submit-icon')
        search_button.click()

        try:
            # Wait for the "Best Match:" link to be clickable
            wait = WebDriverWait(driver, 60, poll_frequency=5, ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            best_match_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Best Match:')]")))

            if best_match_element:
                print('Found best match link')
            else:
                print('No best match link found')
                return None

            # Check to see if a popup window is present
            main_window = driver.current_window_handle
            best_match_element.click()
            time.sleep(10)
            all_windows = driver.window_handles

            # If there is more than one window, switch to the popup window
            if len(all_windows) > 1:
                print('Starting popup window logic...')
                # Loop through all windows and switch to the popup window
                for window in all_windows:
                    if window != main_window:
                        driver.switch_to.window(window)
                        # Wait for the popup window to load, find h1 element
                        course_heading_element = find_element_with_retry(driver, By.CSS_SELECTOR, ".toplevel_popup h1")
                        if course_heading_element:
                            print('Found h1 element')
                        else:
                            print('No h1 element found')
                            return None
                        
                        # Get the course number and course name from the h1 element
                        course_heading_text = course_heading_element.text.strip()
                        course_number, course_name = map(
                            str.strip, course_heading_text.split('-', 1))

                        # Find the popup content block
                        course_text_element = find_element_with_retry(driver, By.CSS_SELECTOR, ".block_content_popup")
                        if course_text_element:
                            print('Found popup content block')
                        else: 
                            print('No popup content block found')
                            return None

                        # Get the course description from the content block
                        course_text = course_text_element.text.strip()

                        # Use regex to find the course description
                        description_pattern = r'DATE OF LAST REVISION:.+\s\s(?P<description>.*)\s\sMAJOR COURSE LEARNING OBJECTIVES'

                        match = re.search(description_pattern,
                                          course_text, re.DOTALL)
                        if match:
                            course_description = match.group(
                                'description').strip()
                        else:
                            course_description = "Not found"

                        # Close the popup window and switch back to the main window
                        driver.close()
                        driver.switch_to.window(main_window)
                        break
            else:
                print('Starting main window logic...')

                # Wait for the main window to load, find h3 element
                course_heading_element = find_element_with_retry(driver, By.XPATH, "//td/div[2]/h3")
                if course_heading_element:
                    print('Found h3 element')
                else:
                    print('No h3 element found')
                    return None

                # Get the course number and course name from the h3 element
                course_heading_text = course_heading_element.text.strip()
                course_number, course_name = map(
                    str.strip, course_heading_text.split('-', 1))

                # Find the content block
                course_text_element = find_element_with_retry(driver, By.XPATH, "//table[2]/tbody/tr[3]/td/table/tbody/tr/td/div[2]")
                if course_text_element:
                    print('Found content block')
                else:
                    print('No content block found')
                    return None

                # Get the course description from the content block
                course_text = course_text_element.text.strip()

                # Use regex to find the course description
                description_pattern = r'DATE OF LAST REVISION:.+\s\s(?P<description>.*)\s\sMAJOR COURSE LEARNING OBJECTIVES'

                match = re.search(description_pattern, course_text, re.DOTALL)
                if match:
                    course_description = match.group('description').strip()
                else:
                    course_description = "Not found"

            # Print the course data
            print(course_number)
            print(course_name)
            print(course_description)

            # Return the course data
            return course_number, course_name, course_description

        except Exception as e:
            # If an error occurs, print a useless message and return None
            print("Error encountered while scraping:", e)
            return None

    finally:
        driver.quit()