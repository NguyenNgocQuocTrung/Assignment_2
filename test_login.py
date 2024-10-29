import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException  # Importing TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

# Tạo fixture cho driver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service
from selenium import webdriver
from selenium.webdriver.edge.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.0.0")
    options.add_argument("--headless")  # Tắt các tiện ích mở rộng
    options.add_argument("--start-maximized")  # Mở cửa sổ trình duyệt ở chế độ tối đa
    options.add_argument("--disable-extensions")  # Tắt các tiện ích mở rộng
    options.add_argument("--disable-infobars")  # Tắt thanh thông báo


    service = Service(EdgeChromiumDriverManager().install())

    driver = webdriver.Edge(service=service, options=options)
    
    yield driver  
    
    driver.quit()  




#STT: 1 Pass
#Test Login and Logout
# def test_login_and_logout(driver):
#     # Navigate to the home page
#     driver.get("https://demo.opencart.com/en-gb?route=common/home")

#     # Wait to ensure the page is fully loaded
#     time.sleep(5)  # Adjust wait time if necessary

#     # Wait for the "My Account" dropdown to be clickable
#     account_dropdown = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.XPATH, "//a[@class='dropdown-toggle' and @data-bs-toggle='dropdown']"))
#     )
#     driver.execute_script("arguments[0].click();", account_dropdown)  # Use JavaScript to click

#     # Wait for the "Login" link to be visible and clickable
#     try:
#         login_link = WebDriverWait(driver, 20).until(
#             EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
#         )
#         driver.execute_script("arguments[0].click();", login_link)  # Click the "Login" link
#     except Exception as e:
#         print("Error locating the Login link:", e)
#         print("Current page source:", driver.page_source)
#         return  # Exit if there's an error

#     # Wait for the email input to appear and fill in login details
#     WebDriverWait(driver, 20).until(
#         EC.presence_of_element_located((By.ID, "input-email"))
#     ).send_keys("quoctrung87377@gmail.com")
#     driver.find_element(By.ID, "input-password").send_keys("Nozdormu1#")
    
#     # Click the submit button
#     driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

#     # Verify successful login by checking the URL
#     WebDriverWait(driver, 20).until(
#         EC.url_contains("account/account")
#     )
#     assert "account/account" in driver.current_url, "Login failed or user not redirected to account page."

#     # Now perform the logout process
#     # Wait for the "My Account" dropdown to be clickable
#     account_dropdown = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.XPATH, "//a[@class='dropdown-toggle' and @data-bs-toggle='dropdown']"))
#     )
#     driver.execute_script("arguments[0].click();", account_dropdown)

#     # Wait for the "Logout" link to be clickable
#     logout_link = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))
#     )
#     driver.execute_script("arguments[0].click();", logout_link)

#     # Wait for the logout to complete and check the URL
#     WebDriverWait(driver, 20).until(
#         EC.url_contains("account/logout")
#     )

#     # Assert logout success by checking if the current URL contains "account/logout"
#     assert "account/logout" in driver.current_url, "Logout was not successful."

#     # Optional: Check if the user is redirected to the homepage after logging out
#     WebDriverWait(driver, 20).until(
#         EC.url_contains("common/home")
#     )
#     assert "common/home" in driver.current_url, "User was not redirected to the homepage after logout."

#STT: 2 Pass
#Test register
# def test_register_and_check_submission(driver):
#     # Navigate to the home page
#     driver.get("https://demo.opencart.com/en-gb?route=common/home")

#     # Wait to ensure the page is fully loaded
#     time.sleep(5)  # Adjust wait time if necessary

#     # Wait for the "My Account" dropdown to be clickable
#     account_dropdown = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.XPATH, "//a[@class='dropdown-toggle' and @data-bs-toggle='dropdown']"))
#     )
#     driver.execute_script("arguments[0].click();", account_dropdown)  # Use JavaScript to click

#     # Explicitly wait for the dropdown to expand and the "Register" link to be present
#     time.sleep(1)  # This can be adjusted if necessary

#     # Try locating the "Register" link using different locators
#     try:
#         register_link = WebDriverWait(driver, 20).until(
#             EC.element_to_be_clickable((By.XPATH, "//a[text()='Register']"))
#         )
#         driver.execute_script("arguments[0].click();", register_link)
#     except TimeoutException:
#         print("Register link not found or not clickable.")
#         print("Current URL:", driver.current_url)
#         print("Page source:", driver.page_source)  # For debugging
#         driver.quit()
#         return

#     # Fill in the registration form
#     driver.find_element(By.ID, "input-firstname").send_keys("John")  # First Name
#     driver.find_element(By.ID, "input-lastname").send_keys("Doe")    # Last Name
#     driver.find_element(By.ID, "input-email").send_keys("john.doe@example.com")  # Email
#     driver.find_element(By.ID, "input-telephone").send_keys("1234567890")  # Telephone
#     driver.find_element(By.ID, "input-password").send_keys("password123")  # Password
#     driver.find_element(By.ID, "input-confirm").send_keys("password123")   # Confirm Password

#     # Click the privacy policy checkbox
#     privacy_checkbox = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.NAME, "agree"))
#     )
#     driver.execute_script("arguments[0].click();", privacy_checkbox)

#     # Submit the registration form
#     submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
#     driver.execute_script("arguments[0].click();", submit_button)

#     # Verify successful registration
#     # Wait for the success message or check for specific URL
#     try:
#         WebDriverWait(driver, 20).until(
#             EC.presence_of_element_located((By.XPATH, "//h1[text()='Your Account Has Been Created!']"))
#         )
#         print("Registration successful. User account created.")
        
#         # Optionally, check if the user is redirected to the account page
#         WebDriverWait(driver, 20).until(
#             EC.url_contains("account/account")
#         )
#     except Exception as e:
#         print("Registration failed or success message not found:", e)
#         print("Current page source:", driver.page_source)
#         return

#STT: 3 Pass
#test navigation
# def test_navigation(driver):
#     # Navigate to the home page
#     driver.get("https://demo.opencart.com/en-gb?route=common/home")

#     # Wait to ensure the page is fully loaded
#     time.sleep(3)  # Adjust wait time if necessary

#     # Check navigation to the Products page
#     try:
#         products_link = WebDriverWait(driver, 20).until(
#             EC.element_to_be_clickable((By.LINK_TEXT, "Desktops")))
#         products_link.click()

#         # Wait and verify navigation
#         WebDriverWait(driver, 20).until(
#             EC.title_contains("Desktops"))  # Check if the title contains 'Desktops'
#         print("Navigated to Products page:", driver.title)

#         # Short wait before clicking the specific product link
#         time.sleep(2)

#         # Navigate to a specific product
#         specific_product_link = WebDriverWait(driver, 20).until(
#             EC.presence_of_element_located((By.LINK_TEXT, "MacBook")))  # Wait for the element to be present

#         # Debug: Check if the link is clickable
#         print("Product link is clickable:", specific_product_link.is_displayed())
        
#         # Click the specific product link
#         driver.execute_script("arguments[0].click();", specific_product_link)  # Force click using JavaScript

#         # Wait and verify navigation to product details
#         WebDriverWait(driver, 20).until(
#             EC.title_contains("MacBook"))  # Check if the title contains 'MacBook'
#         print("Navigated to specific product page:", driver.title)

#     except TimeoutException:
#         print("Timeout while waiting for the product link to be clickable.")
#     except Exception as e:
#         print("An error occurred:", e)
#     finally:
#         # Clean up and close the driver
#         driver.quit()

#STT: 4 Pass
#Test error handling
# def test_empty_required_field(driver):
#     driver.get("https://demo.opencart.com/index.php?route=account/register")

#     # Attempt to submit the form without filling any fields
#     try:
#         # Wait for the "Continue" button to be clickable and then click it
#         submit_button = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, "//button[text()='Continue']"))
#         )
#         submit_button.click()

#         # Wait for the error message to be displayed
#         error_message = WebDriverWait(driver, 10).until(
#             EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-danger"))
#         )
        
#         # Check the error message for specific text
#         assert "E-Mail Address must be between 1 and 32 characters!" in error_message.text
#         print("Empty required field test passed.")
    
#     except TimeoutException:
#         print("Error message for empty required field did not appear.")
#     except NoSuchElementException:
#         print("Submit button not found. Please check the locator.")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

#STT: 5
# Sample data for validation
#Để sau_đang fail
# expected_data = {
#     "total_users": "1000",  # Expected value for total users
#     "active_users": "800",   # Expected value for active users
#     "new_signups": "50"      # Expected value for new signups
# }

# def test_dashboard_data_validation(driver):
#     # Navigate to the dashboard page
#     driver.get("https://demo.opencart.com/admin/index.php?route=dashboard")  # Update with your dashboard URL

#     # Wait for the dashboard to load
#     WebDriverWait(driver, 20).until(
#         EC.visibility_of_element_located((By.XPATH, "//h1[text()='Dashboard']"))
#     )

#     # Validate total users
#     total_users_element = driver.find_element(By.XPATH, "//div[@id='total-users']")  # Update the XPath
#     assert total_users_element.text == expected_data["total_users"], f"Expected {expected_data['total_users']} for total users, but got {total_users_element.text}"

#     # Validate active users
#     active_users_element = driver.find_element(By.XPATH, "//div[@id='active-users']")  # Update the XPath
#     assert active_users_element.text == expected_data["active_users"], f"Expected {expected_data['active_users']} for active users, but got {active_users_element.text}"

#     # Validate new signups
#     new_signups_element = driver.find_element(By.XPATH, "//div[@id='new-signups']")  # Update the XPath
#     assert new_signups_element.text == expected_data["new_signups"], f"Expected {expected_data['new_signups']} for new signups, but got {new_signups_element.text}"

#     print("All data validations passed successfully.")

#STT: 6_Pass
#test search
# def search_products(driver):
#     # Open the homepage
#     driver.get("https://demo.opencart.com/en-gb?route=common/home")  # Update with your application's URL
#     search_query = "MacBook"
#     try:
#         # Locate the search input box
#         search_box = WebDriverWait(driver, 30).until(
#             EC.visibility_of_element_located((By.NAME, "search"))
#         )

#         # Perform a search
#         search_box.clear()
#         search_box.send_keys(search_query + Keys.RETURN)  # Submit the search

#         # Wait for the search results to load
#         WebDriverWait(driver, 20).until(
#             EC.presence_of_element_located((By.ID, "product-list"))
#         )

#         # Locate product elements
#         products = driver.find_elements(By.XPATH, "//div[@id='product-list']//div[@class='product-thumb']")

#         # List to store product details
#         product_details = []

#         # Check if products were found
#         if not products:
#             print("No products found for the search query.")
#             return product_details  # Return an empty list if no products found

#         for product in products:
#             # Extract product details
#             product_name = product.find_element(By.XPATH, ".//h4/a").text
#             product_price = product.find_element(By.XPATH, ".//span[@class='price-new']").text
#             product_link = product.find_element(By.XPATH, ".//h4/a").get_attribute('href')

#             # Store product details in a dictionary
#             product_details.append({
#                 "name": product_name,
#                 "price": product_price,
#                 "link": product_link
#             })

#             # Print product details (optional)
#             print(f"Product Name: {product_name}")
#             print(f"Price: {product_price}")
#             print(f"Link: {product_link}")
#             print("=" * 40)  # Separator for better readability

#         return product_details  # Return the list of product details

#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return []  # Return an empty list if an error occurs
    

# def test_search_products(driver):
#     results = search_products(driver)
#     assert len(results) > 0, "No products found for 'MacBook'"

#STT: 7_Pass
# Function to test the application's responsiveness
def test_responsive_design(driver):
    # Define different screen sizes to test
    screen_sizes = [
        (1920, 1080),  # Desktop
        (1366, 768),   # Laptop
        (768, 1024),   # Tablet
        (375, 667),    # Mobile (iPhone 6/7/8)
        (414, 896),    # Mobile (iPhone XR)
    ]

    for width, height in screen_sizes:
        driver.set_window_size(width, height)  # Set the browser window size
        driver.get("https://demo.opencart.com/en-gb?route=common/home")  # Your application's URL

        try:
            # Wait for the header to be visible
            header = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "header"))
            )
            assert header.is_displayed(), f"Header is not displayed at {width}x{height}"

            # Wait for the search box to be visible
            search_box = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.NAME, "search"))
            )
            assert search_box.is_displayed(), f"Search box is not displayed at {width}x{height}"

            # Print the current screen size being tested
            print(f"Tested screen size: {width}x{height}")

        except Exception as e:
            print(f"Error during testing at {width}x{height}: {e}")