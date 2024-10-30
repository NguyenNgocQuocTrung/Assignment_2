import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("driver")  # Sử dụng fixture driver đã định nghĩa
def login(driver):
    # Mở trang đăng nhập
    driver.get("https://demo.opencart.com/index.php?route=account/login")

    # Khởi tạo WebDriverWait với thời gian chờ tối đa
    wait = WebDriverWait(driver, 10)  # Thay đổi 10 thành thời gian chờ tối đa bạn mong muốn

    # Chờ cho trường email có thể nhìn thấy và nhập email
    email_field = wait.until(EC.visibility_of_element_located((By.ID, "input-email")))
    email_field.send_keys("quoctrung87377@gmail.com")

    # Chờ cho trường mật khẩu có thể nhìn thấy và nhập mật khẩu
    password_field = wait.until(EC.visibility_of_element_located((By.ID, "input-password")))
    password_field.send_keys("Nozdormu1#")

    time.sleep(10)  # Chờ trang tải xong

    # Chờ cho nút đăng nhập có thể nhấp được và nhấn
    login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))
    login_button.click()

    # Chờ cho việc đăng nhập hoàn tất (kiểm tra tiêu đề trang hoặc một phần tử nào đó)
    wait.until(EC.title_contains("My Account"))  # Kiểm tra tiêu đề trang nếu đăng nhập thành công
    
    
    
def test_checkout_valid_info(driver):
    # Đăng nhập vào tài khoản
    login(driver)
    # Chọn sản phẩm để thêm vào giỏ hàng
    driver.get("https://demo.opencart.com/index.php?route=product/product&product_id=43")  # Cập nhật với ID sản phẩm hợp lệ
    wait = WebDriverWait(driver, 10)
    
    time.sleep(10)  # Chờ trang tải xong
    # Thêm sản phẩm vào giỏ hàng
    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.ID, "button-cart")))
    add_to_cart_button.click()
    time.sleep(10)  # Chờ trang tải xong

    # Đi đến giỏ hàng
    driver.get("https://demo.opencart.com/index.php?route=checkout/cart")
    
    time.sleep(10)  # Chờ giỏ hàng cập nhật

    # Chọn nút thanh toán
    checkout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Checkout")))
    checkout_button.click()
    
    time.sleep(10)  # Chờ trang thanh toán tải xong

    # Nhập thông tin thanh toán hợp lệ
    wait.until(EC.visibility_of_element_located((By.ID, "input-payment-firstname"))).send_keys("John")
    wait.until(EC.visibility_of_element_located((By.ID, "input-payment-lastname"))).send_keys("Doe")
    wait.until(EC.visibility_of_element_located((By.ID, "input-payment-address-1"))).send_keys("123 Main St")
    wait.until(EC.visibility_of_element_located((By.ID, "input-payment-city"))).send_keys("New York")
    wait.until(EC.visibility_of_element_located((By.ID, "input-payment-postcode"))).send_keys("10001")
    wait.until(EC.visibility_of_element_located((By.ID, "input-payment-country"))).send_keys("United States")
    wait.until(EC.visibility_of_element_located((By.ID, "input-payment-zone"))).send_keys("New York")

    # Chọn phương thức thanh toán
    payment_method_radio = wait.until(EC.element_to_be_clickable((By.NAME, "payment_method")))
    payment_method_radio.click()

    # Xác nhận đặt hàng
    confirm_order_button = wait.until(EC.element_to_be_clickable((By.ID, "button-confirm")))
    confirm_order_button.click()

    # Kiểm tra xem thông báo thành công có hiển thị hay không
    success_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success")))
    assert "Your order has been placed!" in success_message.text




# def test_checkout_no_choose_methods(driver):
#     # Đăng nhập vào tài khoản
#     login(driver)

#     # Chọn sản phẩm để thêm vào giỏ hàng
#     driver.get("https://demo.opencart.com/index.php?route=product/product&product_id=43")  # Cập nhật với ID sản phẩm hợp lệ
#     wait = WebDriverWait(driver, 10)
    
#     # Thêm sản phẩm vào giỏ hàng
#     add_to_cart_button = wait.until(EC.element_to_be_clickable((By.ID, "button-cart")))
#     add_to_cart_button.click()

#     # Đi đến giỏ hàng
#     driver.get("https://demo.opencart.com/index.php?route=checkout/cart")

#     # Chọn nút thanh toán
#     checkout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Checkout")))
#     checkout_button.click()

#     # Nhập thông tin thanh toán hợp lệ
#     wait.until(EC.visibility_of_element_located((By.ID, "input-payment-firstname"))).send_keys("John")
#     wait.until(EC.visibility_of_element_located((By.ID, "input-payment-lastname"))).send_keys("Doe")
#     wait.until(EC.visibility_of_element_located((By.ID, "input-payment-address-1"))).send_keys("123 Main St")
#     wait.until(EC.visibility_of_element_located((By.ID, "input-payment-city"))).send_keys("New York")
#     wait.until(EC.visibility_of_element_located((By.ID, "input-payment-postcode"))).send_keys("10001")
#     wait.until(EC.visibility_of_element_located((By.ID, "input-payment-country"))).send_keys("United States")
#     wait.until(EC.visibility_of_element_located((By.ID, "input-payment-zone"))).send_keys("New York")

#     # Không chọn phương thức thanh toán (bỏ qua bước này)

#     # Xác nhận đặt hàng mà không chọn phương thức thanh toán
#     confirm_order_button = wait.until(EC.element_to_be_clickable((By.ID, "button-confirm")))
#     confirm_order_button.click()

#     # Kiểm tra xem thông báo lỗi có hiển thị hay không
#     error_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-danger")))
#     assert "Warning: Please select a payment method!" in error_message.text



# def test_checkout_empty_input(driver):
#     # Đăng nhập vào tài khoản
#     login(driver)

#     # Chọn sản phẩm để thêm vào giỏ hàng
#     driver.get("https://demo.opencart.com/index.php?route=product/product&product_id=43")  # Cập nhật với ID sản phẩm hợp lệ
#     wait = WebDriverWait(driver, 10)
    
#     # Thêm sản phẩm vào giỏ hàng
#     add_to_cart_button = wait.until(EC.element_to_be_clickable((By.ID, "button-cart")))
#     add_to_cart_button.click()

#     # Đi đến giỏ hàng
#     driver.get("https://demo.opencart.com/index.php?route=checkout/cart")

#     # Chọn nút thanh toán
#     checkout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Checkout")))
#     checkout_button.click()

#     # Nhập thông tin thanh toán nhưng để trống
#     # Bỏ qua bước nhập thông tin cần thiết

#     # Nhấn nút xác nhận đơn hàng
#     confirm_order_button = wait.until(EC.element_to_be_clickable((By.ID, "button-confirm")))
#     confirm_order_button.click()

#     # Kiểm tra xem thông báo lỗi có hiển thị hay không
#     error_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-danger")))
#     assert "Warning: You must provide address information!" in error_message.text


# def test_checkout_above_upper_boundary(driver):
#     # Đăng nhập vào tài khoản
#     login(driver)

#     # Chọn sản phẩm để thêm vào giỏ hàng
#     driver.get("https://demo.opencart.com/index.php?route=product/product&product_id=43")  # Cập nhật với ID sản phẩm hợp lệ
#     wait = WebDriverWait(driver, 10)
    
#     # Thêm sản phẩm vào giỏ hàng
#     add_to_cart_button = wait.until(EC.element_to_be_clickable((By.ID, "button-cart")))
#     add_to_cart_button.click()

#     # Đi đến giỏ hàng
#     driver.get("https://demo.opencart.com/index.php?route=checkout/cart")

#     # Chọn nút thanh toán
#     checkout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Checkout")))
#     checkout_button.click()

#     # Nhập thông tin thanh toán với các trường vượt quá giới hạn
#     wait.until(EC.visibility_of_element_located((By.ID, "input-firstname"))).send_keys("A" * 256)  # Giả sử giới hạn là 255 ký tự
#     wait.until(EC.visibility_of_element_located((By.ID, "input-lastname"))).send_keys("B" * 256)
#     wait.until(EC.visibility_of_element_located((By.ID, "input-address-1"))).send_keys("C" * 256)
#     wait.until(EC.visibility_of_element_located((By.ID, "input-city"))).send_keys("D" * 256)

#     # Nhấn nút xác nhận đơn hàng
#     confirm_order_button = wait.until(EC.element_to_be_clickable((By.ID, "button-confirm")))
#     confirm_order_button.click()

#     # Kiểm tra xem thông báo lỗi có hiển thị hay không
#     error_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-danger")))
#     assert "Warning: Address does not appear to be valid!" in error_message.text


# def test_checkout_under_lower_boundary(driver):
#     # Đăng nhập vào tài khoản
#     login(driver)

#     # Chọn sản phẩm để thêm vào giỏ hàng
#     driver.get("https://demo.opencart.com/index.php?route=product/product&product_id=43")  # Cập nhật với ID sản phẩm hợp lệ
#     wait = WebDriverWait(driver, 10)
    
#     # Thêm sản phẩm vào giỏ hàng
#     add_to_cart_button = wait.until(EC.element_to_be_clickable((By.ID, "button-cart")))
#     add_to_cart_button.click()

#     # Đi đến giỏ hàng
#     driver.get("https://demo.opencart.com/index.php?route=checkout/cart")

#     # Chọn nút thanh toán
#     checkout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Checkout")))
#     checkout_button.click()

#     # Nhập thông tin thanh toán với các trường dưới giới hạn
#     wait.until(EC.visibility_of_element_located((By.ID, "input-firstname"))).send_keys("")  # Nhập trống
#     wait.until(EC.visibility_of_element_located((By.ID, "input-lastname"))).send_keys("")
#     wait.until(EC.visibility_of_element_located((By.ID, "input-address-1"))).send_keys("")
#     wait.until(EC.visibility_of_element_located((By.ID, "input-city"))).send_keys("")

#     # Nhấn nút xác nhận đơn hàng
#     confirm_order_button = wait.until(EC.element_to_be_clickable((By.ID, "button-confirm")))
#     confirm_order_button.click()

#     # Kiểm tra xem thông báo lỗi có hiển thị hay không
#     error_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-danger")))
#     assert "Warning: Please enter your first name!" in error_message.text