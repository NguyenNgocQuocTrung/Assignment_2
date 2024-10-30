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
from selenium.webdriver.support.ui import Select

import pytest
@pytest.mark.usefixtures("driver")  # Sử dụng fixture driver đã định nghĩa

def test_checkout_with_guest_account(driver):
 #     # Mở trang sản phẩm
    driver.get("https://demo.opencart.com/index.php?route=product/product&product_id=43")  # Cập nhật với ID sản phẩm hợp lệ
    wait = WebDriverWait(driver, 10)
    
    time.sleep(10)  # Chờ trang tải xong
    # Thêm sản phẩm vào giỏ hàng
    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.ID, "button-cart")))
    add_to_cart_button.click()
    time.sleep(10)  # Chờ trang tải xong

    # Đi đến giỏ hàng
    driver.get("https://demo.opencart.com/index.php?route=checkout/cart")

    time.sleep(10)  # Chờ trang tải xong

    # Nhấn nút thanh toán
    checkout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Checkout")))
    checkout_button.click()

    time.sleep(10)  # Chờ trang tải xong
    # Chọn tài khoản khách
    input_guest = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-guest"))
    )
    input_guest.click()
    time.sleep(1)

   # Nhập thông tin khách hàng
    first_name = "Trung"
    last_name = "Nguyen"
    email = "nguyentrung@gmail.com"
    company = "Company ABC"
    address1 = "Quan 1"
    address2 = "Quan 5"
    city = "Ho Chi Minh City"
    post_code = "700000"
    country = "Viet Nam"
    region = "Ho Chi Minh City"

    input_first_name = driver.find_element(By.CSS_SELECTOR, "#input-firstname")
    input_first_name.send_keys(first_name)
    time.sleep(1)

    input_last_name = driver.find_element(By.CSS_SELECTOR, "#input-lastname")
    input_last_name.send_keys(last_name)
    time.sleep(1)

    input_email = driver.find_element(By.CSS_SELECTOR, "#input-email")
    input_email.send_keys(email)
    time.sleep(1)

    input_company = driver.find_element(By.CSS_SELECTOR, "#input-shipping-company")
    input_company.send_keys(company)
    time.sleep(1)

    input_address1 = driver.find_element(By.CSS_SELECTOR, "#input-shipping-address-1")
    input_address1.send_keys(address1)
    time.sleep(1)

    input_address2 = driver.find_element(By.CSS_SELECTOR, "#input-shipping-address-2")
    driver.execute_script("arguments[0].scrollIntoView(true);", input_address2)
    time.sleep(1)
    input_address2.send_keys(address2)

    input_city = driver.find_element(By.CSS_SELECTOR, "#input-shipping-city")
    input_city.send_keys(city)
    time.sleep(1)

    input_post_code = driver.find_element(By.CSS_SELECTOR, "#input-shipping-postcode")
    input_post_code.clear()
    input_post_code.send_keys(post_code)
    time.sleep(1)

    input_country = driver.find_element(By.CSS_SELECTOR, "#input-shipping-country")
    selection_country = Select(input_country)
    selection_country.select_by_visible_text(country)
    time.sleep(1)

    input_region = driver.find_element(By.CSS_SELECTOR, "#input-shipping-zone")
    selection_region = Select(input_region)
    selection_region.select_by_visible_text(region)
    time.sleep(1)

    continue_btn = driver.find_element(By.CSS_SELECTOR, "#button-register")
    continue_btn.click()
    time.sleep(5)

    shipping_method = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#button-shipping-methods"))
    )
    shipping_method.click()

    method_flat = driver.find_element(By.CSS_SELECTOR, "#input-shipping-method-flat-flat")
    method_flat.click()
    time.sleep(1)

    continue_1 = driver.find_element(By.CSS_SELECTOR, "#button-shipping-method")
    continue_1.click()
    time.sleep(1)

    payment_method = driver.find_element(By.CSS_SELECTOR, "#button-payment-methods")
    payment_method.click()
    time.sleep(1)

    cash_method = driver.find_element(By.CSS_SELECTOR, "#input-payment-method-cod-cod")
    cash_method.click()
    time.sleep(1)

    continue_2 = driver.find_element(By.CSS_SELECTOR, "#button-payment-method")
    continue_2.click()
    time.sleep(1)

    confirm_order = driver.find_element(By.CSS_SELECTOR, "#button-confirm")
    confirm_order.click()
    time.sleep(1)

    notification = driver.find_element(By.CSS_SELECTOR, "#content > h1")
    notification_actual = notification.text

    notification_expected = "Your order has been placed!"

    assert notification_expected == notification_actual, "Đơn hàng không được đặt thành công"


def test_guest_account_empty_required_input(driver):
 #     # Mở trang sản phẩm
    driver.get("https://demo.opencart.com/index.php?route=product/product&product_id=43")  # Cập nhật với ID sản phẩm hợp lệ
    wait = WebDriverWait(driver, 10)
    
    time.sleep(10)  # Chờ trang tải xong
    # Thêm sản phẩm vào giỏ hàng
    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.ID, "button-cart")))
    add_to_cart_button.click()
    time.sleep(10)  # Chờ trang tải xong

    # Đi đến giỏ hàng
    driver.get("https://demo.opencart.com/index.php?route=checkout/cart")

    time.sleep(10)  # Chờ trang tải xong

    # Nhấn nút thanh toán
    checkout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Checkout")))
    checkout_button.click()

    time.sleep(10)  # Chờ trang tải xong
    # Chọn tài khoản khách
    input_guest = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-guest"))
    )
    input_guest.click()
    time.sleep(1)

    # Nhấn nút tiếp tục mà không điền thông tin bắt buộc
    continue_btn = driver.find_element(By.CSS_SELECTOR, "#button-register")
    continue_btn.click()
    time.sleep(1)

    # Kiểm tra thông báo lỗi
    error_notification = driver.find_element(By.CSS_SELECTOR, ".alert.alert-danger")  # Cập nhật CSS selector cho thông báo lỗi
    error_notification_text = error_notification.text

    # Kiểm tra thông báo lỗi
    expected_error_message = "Warning: First Name must be between 1 and 32 characters!"  # Thay đổi thông báo tùy thuộc vào hệ thống
    assert expected_error_message in error_notification_text, "Thông báo lỗi không chính xác khi không điền trường bắt buộc"


def test_guest_account_lower_boundary(driver):
    # Mở trang sản phẩm
    driver.get("https://demo.opencart.com/index.php?route=product/product&product_id=43")  # Cập nhật với ID sản phẩm hợp lệ
    wait = WebDriverWait(driver, 10)

    time.sleep(10)  # Chờ trang tải xong
    # Thêm sản phẩm vào giỏ hàng
    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.ID, "button-cart")))
    add_to_cart_button.click()

    time.sleep(10)  # Chờ trang tải xong

    # Đi đến giỏ hàng
    driver.get("https://demo.opencart.com/index.php?route=checkout/cart")

    time.sleep(10)  # Chờ trang tải xong
    
    # Nhấn nút thanh toán
    checkout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Checkout")))
    checkout_button.click()
    
    time.sleep(10)  # Chờ trang tải xong

    # Nhập thông tin khách hàng với dữ liệu ở giới hạn dưới
    # Ví dụ: nhập tên ngắn hơn giới hạn cho phép
    first_name_field = wait.until(EC.visibility_of_element_located((By.ID, "input-payment-firstname")))
    first_name_field.clear()
    first_name_field.send_keys("A")  # Tên quá ngắn

    last_name_field = wait.until(EC.visibility_of_element_located((By.ID, "input-payment-lastname")))
    last_name_field.clear()
    last_name_field.send_keys("B")  # Họ quá ngắn

    email_field = wait.until(EC.visibility_of_element_located((By.ID, "input-payment-email")))
    email_field.clear()
    email_field.send_keys("test@a.com")  # Địa chỉ email ngắn

    telephone_field = wait.until(EC.visibility_of_element_located((By.ID, "input-payment-telephone")))
    telephone_field.clear()
    telephone_field.send_keys("123")  # Số điện thoại quá ngắn

    # Nhấn nút xác nhận đơn hàng
    confirm_order_button = wait.until(EC.element_to_be_clickable((By.ID, "button-confirm")))
    confirm_order_button.click()

    # Kiểm tra thông báo lỗi cho các trường thông tin không hợp lệ
    error_messages = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".alert.alert-danger")))
    
    # Kiểm tra xem có thông báo lỗi hay không
    assert len(error_messages) > 0, "Expected error messages for lower boundary input were not found."
    
    # In ra thông báo lỗi (tuỳ chọn)
    for message in error_messages:
        print(message.text)

def test_guest_account_upper_boundary(driver):
        driver.get("https://demo.opencart.com/index.php?route=product/product&product_id=43")  # Cập nhật với ID sản phẩm hợp lệ
        wait = WebDriverWait(driver, 10)
        
        time.sleep(10)  # Chờ trang tải xong
        # Thêm sản phẩm vào giỏ hàng
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.ID, "button-cart")))
        add_to_cart_button.click()
        time.sleep(10)  # Chờ trang tải xong

        # Đi đến giỏ hàng
        driver.get("https://demo.opencart.com/index.php?route=checkout/cart")

        time.sleep(10)  # Chờ trang tải xong

        # Nhấn nút thanh toán
        checkout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Checkout")))
        checkout_button.click()

        time.sleep(10)  # Chờ trang tải xong
        # Chọn tài khoản khách
        input_guest = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-guest"))
        )
        input_guest.click()
        time.sleep(1)

        # Nhập thông tin khách hàng với dữ liệu giới hạn trên
        first_name = "A" * 32  # Giới hạn ký tự
        last_name = "B" * 32   # Giới hạn ký tự
        email = "example@example.com"
        company = "Company ABC"
        address1 = "Street Name " + "C" * 64  # Giới hạn ký tự
        address2 = "Block " + "D" * 64  # Giới hạn ký tự
        city = "Ho Chi Minh City"
        post_code = "700000"
        country = "Viet Nam"
        region = "Ho Chi Minh City"

        # Nhập thông tin khách hàng
#     first_name = "Trung"
#     last_name = "Nguyen"
#     email = "nguyentrung@gmail.com"
#     company = "Company ABC"
#     address1 = "Quan 1"
#     address2 = "Quan 5"
#     city = "Ho Chi Minh City"
#     post_code = "700000"
#     country = "Viet Nam"
#     region = "Ho Chi Minh City"

        input_first_name = driver.find_element(By.CSS_SELECTOR, "#input-firstname")
        input_first_name.send_keys(first_name)
        time.sleep(1)

        input_last_name = driver.find_element(By.CSS_SELECTOR, "#input-lastname")
        input_last_name.send_keys(last_name)
        time.sleep(1)

        input_email = driver.find_element(By.CSS_SELECTOR, "#input-email")
        input_email.send_keys(email)
        time.sleep(1)

        input_company = driver.find_element(By.CSS_SELECTOR, "#input-shipping-company")
        input_company.send_keys(company)
        time.sleep(1)

        input_address1 = driver.find_element(By.CSS_SELECTOR, "#input-shipping-address-1")
        input_address1.send_keys(address1)
        time.sleep(1)

        input_address2 = driver.find_element(By.CSS_SELECTOR, "#input-shipping-address-2")
        driver.execute_script("arguments[0].scrollIntoView(true);", input_address2)
        time.sleep(1)
        input_address2.send_keys(address2)

        input_city = driver.find_element(By.CSS_SELECTOR, "#input-shipping-city")
        input_city.send_keys(city)
        time.sleep(1)

        input_post_code = driver.find_element(By.CSS_SELECTOR, "#input-shipping-postcode")
        input_post_code.clear()
        input_post_code.send_keys(post_code)
        time.sleep(1)

        input_country = driver.find_element(By.CSS_SELECTOR, "#input-shipping-country")
        selection_country = Select(input_country)
        selection_country.select_by_visible_text(country)
        time.sleep(1)

        input_region = driver.find_element(By.CSS_SELECTOR, "#input-shipping-zone")
        selection_region = Select(input_region)
        selection_region.select_by_visible_text(region)
        time.sleep(1)

        continue_btn = driver.find_element(By.CSS_SELECTOR, "#button-register")
        continue_btn.click()
        time.sleep(5)

        shipping_method = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#button-shipping-methods"))
        )
        shipping_method.click()

        method_flat = driver.find_element(By.CSS_SELECTOR, "#input-shipping-method-flat-flat")
        method_flat.click()
        time.sleep(1)

        continue_1 = driver.find_element(By.CSS_SELECTOR, "#button-shipping-method")
        continue_1.click()
        time.sleep(1)

        payment_method = driver.find_element(By.CSS_SELECTOR, "#button-payment-methods")
        payment_method.click()
        time.sleep(1)

        cash_method = driver.find_element(By.CSS_SELECTOR, "#input-payment-method-cod-cod")
        cash_method.click()
        time.sleep(1)

        continue_2 = driver.find_element(By.CSS_SELECTOR, "#button-payment-method")
        continue_2.click()
        time.sleep(1)

        confirm_order = driver.find_element(By.CSS_SELECTOR, "#button-confirm")
        confirm_order.click()
        time.sleep(1)



        # Xác minh rằng thông báo hiển thị rằng đơn hàng đã được đặt thành công
        notification = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#content > h1"))
        )
        notification_actual = notification.text
        notification_expected = "Your order has been placed!"
        assert(notification_expected, notification_actual, "Order was not placed successfully")