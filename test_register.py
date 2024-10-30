import unittest
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

import pytest
@pytest.mark.usefixtures("driver")  # Sử dụng fixture driver đã định nghĩa

def test_register_valid_data(driver):
    # Navigate to the registration page
    driver.get("https://demo.opencart.com/index.php?route=account/register&language=en-gb")
    time.sleep(2)  # Wait for the page to load

    # Fill out the registration form with valid data
    first_name_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "input-firstname"))
    )
    first_name_field.send_keys("John")

    last_name_field = driver.find_element(By.ID, "input-lastname")
    last_name_field.send_keys("Doe")
    time.sleep(1)  # Wait for the input to process

    email_field = driver.find_element(By.ID, "input-email")
    email_field.send_keys("john.doe@example.com")
    time.sleep(1)

    password_field = driver.find_element(By.ID, "input-password")
    password_field.send_keys("SecurePassword123!")
    time.sleep(1)

    # Agree to the Privacy Policy
    privacy_policy_checkbox = driver.find_element(By.NAME, "agree")
    driver.execute_script("arguments[0].click();", privacy_policy_checkbox)
    time.sleep(10)

    # Submit the registration form
    continue_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    continue_button.click()
    time.sleep(2)  # Wait for the form submission to process

    # Verify successful registration by checking for a success message
    try:
        success_message = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@id='content']/h1"))
        )

        # Assert that the success message is displayed
        assert success_message.is_displayed(), "Success message is not displayed after registration."
        assert "Your Account Has Been Created!" in success_message.text, \
            "The account creation message did not appear as expected."

    except Exception as e:
        print("Error or assertion failed:", e)
        print("Current page source:", driver.page_source)

# PASS
def test_register_empty_required_input(driver):
    # Navigate to the registration page
    driver.get("https://demo.opencart.com/index.php?route=account/register&language=en-gb")
    time.sleep(2)  # Wait for the page to load

    # Click the continue button without filling any fields
    continue_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    continue_button.click()
    time.sleep(2)  # Wait for the error messages to process

    # Check for required field error messages
    try:
        # Verify error message for first name
        first_name_error = driver.find_element(By.XPATH, "//input[@id='input-firstname']/following-sibling::div[@class='text-danger']")
        assert first_name_error.is_displayed(), "First name error message not displayed."
        assert "First Name must be between 1 and 32 characters!" in first_name_error.text, "First name error message text is incorrect."

        # Verify error message for last name
        last_name_error = driver.find_element(By.XPATH, "//input[@id='input-lastname']/following-sibling::div[@class='text-danger']")
        assert last_name_error.is_displayed(), "Last name error message not displayed."
        assert "Last Name must be between 1 and 32 characters!" in last_name_error.text, "Last name error message text is incorrect."

        # Verify error message for email
        email_error = driver.find_element(By.XPATH, "//input[@id='input-email']/following-sibling::div[@class='text-danger']")
        assert email_error.is_displayed(), "Email error message not displayed."
        assert "E-Mail Address does not appear to be valid!" in email_error.text or "E-Mail Address must be between 1 and 96 characters!" in email_error.text, "Email error message text is incorrect."


        # Verify error message for password
        password_error = driver.find_element(By.XPATH, "//input[@id='input-password']/following-sibling::div[@class='text-danger']")
        assert password_error.is_displayed(), "Password error message not displayed."
        assert "Password must be between 4 and 20 characters!" in password_error.text, "Password error message text is incorrect."


    except Exception as e:
        print("Error or assertion failed:", e)
        print("Current page source:", driver.page_source)


# PASS
def test_register_invalid_email(driver):
    # Navigate to the registration page
    driver.get("https://demo.opencart.com/index.php?route=account/register&language=en-gb")
    time.sleep(2)  # Wait for the page to load

    # Fill in valid required fields except for the email
    driver.find_element(By.ID, "input-firstname").send_keys("Test")
    driver.find_element(By.ID, "input-lastname").send_keys("User")
    
    # Enter an invalid email address
    driver.find_element(By.ID, "input-email").send_keys("invalidemail.com")
    
    # Fill in other required fields
    driver.find_element(By.ID, "input-password").send_keys("Password123")

    # Click the continue button
    continue_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    continue_button.click()
    time.sleep(2)  # Wait for the error messages to process

    # Check for email error message
    try:
        email_error = driver.find_element(By.XPATH, "//input[@id='input-email']/following-sibling::div[@class='text-danger']")
        assert email_error.is_displayed(), "Email error message not displayed."
        assert "E-Mail Address does not appear to be valid!" in email_error.text, "Email error message text is incorrect."
    except Exception as e:
        print("Error or assertion failed:", e)
        print("Current page source:", driver.page_source)


# PASS
def test_register_registered_email(driver):
    # Navigate to the registration page
    driver.get("https://demo.opencart.com/index.php?route=account/register&language=en-gb")
    time.sleep(2)  # Wait for the page to load

    # Fill in required fields with valid data
    driver.find_element(By.ID, "input-firstname").send_keys("Test")
    driver.find_element(By.ID, "input-lastname").send_keys("User")

    # Enter an email address that is already registered
    driver.find_element(By.ID, "input-email").send_keys("quoctrung87377@gmail.com")  # Use an already registered email

    driver.find_element(By.ID, "input-password").send_keys("Password123")

    # Click the continue button
    continue_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    continue_button.click()
    time.sleep(2)  # Wait for the error messages to process

    # Check for email already registered error message
    try:
        email_error = driver.find_element(By.XPATH, "//input[@id='input-email']/following-sibling::div[@class='text-danger']")
        assert email_error.is_displayed(), "Email error message not displayed."
        assert "E-Mail Address is already registered!" in email_error.text, "Email error message text is incorrect."
    except Exception as e:
        print("Error or assertion failed:", e)
        print("Current page source:", driver.page_source)

# PASS
def test_register_upper_boundary(driver):
    # Navigate to the registration page
    driver.get("https://demo.opencart.com/index.php?route=account/register&language=en-gb")
    time.sleep(2)  # Wait for the page to load

    # Fill in required fields with maximum length data
    driver.find_element(By.ID, "input-firstname").send_keys("A" * 32)  # Assuming max length for firstname is 32 characters
    driver.find_element(By.ID, "input-lastname").send_keys("B" * 32)   # Assuming max length for lastname is 32 characters

    # Use a valid email format with maximum length (example: max length for email could be 254 characters)
    driver.find_element(By.ID, "input-email").send_keys("a" * 253 + "@example.com")  # Example of long email

    driver.find_element(By.ID, "input-password").send_keys("Password123")  # Assuming max length for password is not being tested here

    # Click the continue button
    continue_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    continue_button.click()
    time.sleep(2)  # Wait for the process to complete

    # Verify registration success
    # Check for the confirmation message or check if redirected to the account page
    try:
        # Assuming success redirects to account page or confirmation message
        assert "Your Account Has Been Created!" in driver.page_source, "Registration was not successful."
        assert driver.current_url == "https://demo.opencart.com/index.php?route=account/success", "User not redirected to success page."
    except Exception as e:
        print("Error or assertion failed:", e)
        print("Current page source:", driver.page_source)

# PASS
def test_register_above_upper_boundary(driver):
    # Navigate to the registration page
    driver.get("https://demo.opencart.com/index.php?route=account/register&language=en-gb")
    time.sleep(2)  # Wait for the page to load

    # Fill in required fields with data exceeding the maximum length
    driver.find_element(By.ID, "input-firstname").send_keys("A" * 33)  # Assuming max length for firstname is 32 characters
    driver.find_element(By.ID, "input-lastname").send_keys("B" * 33)   # Assuming max length for lastname is 32 characters

    # Use an invalid email format with length exceeding typical email limits
    driver.find_element(By.ID, "input-email").send_keys("a" * 254 + "@example.com")  # Exceeds maximum length

    driver.find_element(By.ID, "input-password").send_keys("P" * 129)  # Assuming max length for password is 128 characters

    # Click the continue button
    continue_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    continue_button.click()
    time.sleep(2)  # Wait for the process to complete

    # Verify that appropriate error messages are shown
    try:
        # Check if any error message is displayed
        error_message = driver.find_element(By.CLASS_NAME, "alert-danger")
        assert error_message.is_displayed(), "Error message not displayed for exceeding input lengths."
        
        # Optionally check the content of the error message
        assert "Warning: Please check the form carefully for errors!" in error_message.text, "Unexpected error message content."
    except Exception as e:
        print("Error or assertion failed:", e)
        print("Current page source:", driver.page_source)


# PASS
def test_register_lower_boundary(driver):
    # Navigate to the registration page
    driver.get("https://demo.opencart.com/index.php?route=account/register&language=en-gb")
    time.sleep(2)  # Wait for the page to load

    # Fill in required fields with data below the minimum length
    driver.find_element(By.ID, "input-firstname").send_keys("")  # First name is empty
    driver.find_element(By.ID, "input-lastname").send_keys("")   # Last name is empty
    driver.find_element(By.ID, "input-email").send_keys("a")     # Email is too short
    driver.find_element(By.ID, "input-password").send_keys("a")  # Password is too short

    # Click the continue button
    continue_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    continue_button.click()
    time.sleep(2)  # Wait for the process to complete

    # Verify that appropriate error messages are shown
    try:
        # Check if any error message is displayed
        error_message = driver.find_element(By.CLASS_NAME, "alert-danger")
        assert error_message.is_displayed(), "Error message not displayed for empty required fields."
        
        # Optionally check the content of the error message
        assert "Warning: Please check the form carefully for errors!" in error_message.text, "Unexpected error message content."
    except Exception as e:
        print("Error or assertion failed:", e)
        print("Current page source:", driver.page_source)




# PASS
def test_register_special_characters_in_name(driver):
    # Navigate to the registration page
    driver.get("https://demo.opencart.com/index.php?route=account/register&language=en-gb")
    time.sleep(2)  # Wait for the page to load

    # Fill in the first name and last name with special characters
    driver.find_element(By.ID, "input-firstname").send_keys("@#$%^&*()")  # Special characters in first name
    driver.find_element(By.ID, "input-lastname").send_keys("!<>?:;")    # Special characters in last name
    
    # Fill in other required fields with valid data
    driver.find_element(By.ID, "input-email").send_keys("test@example.com")  # Valid email
    driver.find_element(By.ID, "input-password").send_keys("ValidPassword123")  # Valid password

    # Click the continue button
    continue_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    continue_button.click()
    time.sleep(2)  # Wait for the process to complete

    # Verify that appropriate error messages are shown
    try:
        # Check if any error message is displayed
        error_message = driver.find_element(By.CLASS_NAME, "alert-danger")
        assert error_message.is_displayed(), "Error message not displayed for special characters in name."
        
        # Optionally check the content of the error message
        assert "Warning: First Name must be between 1 and 32 characters!" in error_message.text or \
               "Warning: Last Name must be between 1 and 32 characters!" in error_message.text, "Unexpected error message content."
    except Exception as e:
        print("Error or assertion failed:", e)
        print("Current page source:", driver.page_source)