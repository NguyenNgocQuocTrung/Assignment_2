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

def test_add_to_cart(driver):
    # Mở trang OpenCart
    driver.get("https://demo.opencart.com/en-gb?route=common/home")
    time.sleep(4)  # Chờ trang web tải

    # Đợi cho đến khi nút "Add to Cart" có thể nhấp được
    wait = WebDriverWait(driver, 10)
    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
        "#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 > div:nth-child(2) > div > div.content > form > div > button:nth-child(1)")))

    # Cuộn đến nút "Add to Cart"
    driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_button)
    time.sleep(1)  # Thời gian chờ ngắn để đảm bảo phần tử đã vào tầm nhìn

    # Nhấn nút "Add to Cart"
    add_to_cart_button.click()

    # Chờ một chút để thông báo thành công xuất hiện
    time.sleep(5)

    # Kiểm tra thông báo thành công
    success_message = driver.find_element(By.CSS_SELECTOR, "#alert > div")
    assert success_message.is_displayed(), "Thông báo thành công không hiển thị!"
    assert "iPhone" in success_message.text, "Không tìm thấy thông báo chứa tên sản phẩm!"




# PASS
def test_add_two_to_cart(driver):
    # Mở trang sản phẩm
    driver.get("https://demo.opencart.com/en-gb/product/macbook")# Thay đổi ID sản phẩm nếu cần
    time.sleep(4)  # Chờ trang web tải
    wait = WebDriverWait(driver, 10)

    # Thêm sản phẩm vào giỏ hàng lần đầu tiên
    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.ID, "button-cart")))
    add_to_cart_button.click()
    time.sleep(5)  # Thời gian chờ để đảm bảo giỏ hàng đã cập nhật

    # Thêm sản phẩm vào giỏ hàng lần thứ hai
    add_to_cart_button.click()
    time.sleep(5)  # Thời gian chờ để đảm bảo giỏ hàng đã cập nhật

    #     # Mở giỏ hàng
    cartButton = driver.find_element(By.CSS_SELECTOR, "#header-cart > div > button")
    driver.execute_script("arguments[0].scrollIntoView(true);", cartButton)
    cartButton.click()
    time.sleep(5)  # Đợi giỏ hàng mở

    # Kiểm tra tên sản phẩm trong giỏ hàng
    productNames = driver.find_elements(By.CSS_SELECTOR, "#header-cart > div > ul > li > table > tbody > tr > td.text-start > a")
    actualProductNames = [name.text for name in productNames]

    # Kiểm tra số lượng sản phẩm
    productQuantities = driver.find_elements(By.CSS_SELECTOR, "#header-cart > div > ul > li > table > tbody > tr > td:nth-child(3)")
    actualQuantities = [int(quantity.text.replace("x", "").strip()) for quantity in productQuantities]
    
    expectedProductNames = 'MacBook'
    expectedQuantities = '2'

    assert sorted(expectedProductNames) == sorted(actualProductNames), "Tên sản phẩm không khớp"
    assert expectedQuantities == actualQuantities, "Số lượng sản phẩm không khớp"


def test_add_different_product_to_cart(driver):
    driver.get("https://demo.opencart.com/en-gb?route=common/home")

    time.sleep(4)  # Chờ trang web tải
    # Tìm nút "Add to Cart" cho sản phẩm thứ hai (ví dụ là iPhone)
    wait = WebDriverWait(driver, 10)
    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
        "#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 > div:nth-child(2) > div > div.content > form > div > button:nth-child(1)")))

    time.sleep(4)  # Chờ trang web tải
    
    # Cuộn đến nút "Add to Cart"
    driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_button)
    time.sleep(4)  # Thời gian chờ ngắn để đảm bảo phần tử đã vào tầm nhìn

    # Nhấn nút "Add to Cart" lần đầu
    add_to_cart_button.click()
    time.sleep(5)  # Thời gian chờ để thông báo hiển thị

    # Truy cập trang sản phẩm thứ hai
    # Ví dụ, thêm sản phẩm Samsung
    driver.get("https://demo.opencart.com/en-gb/product/macbook")  # Thay đổi ID sản phẩm nếu cần
    time.sleep(2)

    time.sleep(10)  # Chờ trang tải xong
#     # Thêm sản phẩm vào giỏ hàng
    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.ID, "button-cart")))
    add_to_cart_button.click()
    time.sleep(10)  # Chờ trang tải xong

    # Mở giỏ hàng
    cartButton = driver.find_element(By.CSS_SELECTOR, "#header-cart > div > button")
    driver.execute_script("arguments[0].scrollIntoView(true);", cartButton)
    cartButton.click()
    time.sleep(5)  # Đợi giỏ hàng mở

    # Kiểm tra tên sản phẩm trong giỏ hàng
    productNames = driver.find_elements(By.CSS_SELECTOR, "#header-cart > div > ul > li > table > tbody > tr > td.text-start > a")
    actualProductNames = [name.text for name in productNames]

    # Kiểm tra số lượng sản phẩm
    productQuantities = driver.find_elements(By.CSS_SELECTOR, "#header-cart > div > ul > li > table > tbody > tr > td:nth-child(3)")
    actualQuantities = [int(quantity.text.replace("x", "").strip()) for quantity in productQuantities]

    # Kiểm tra kết quả
    expectedProductNames = ["iPhone", "MacBook"]  # Tên sản phẩm mà bạn đã thêm
    expectedQuantities = [1, 1]  # Số lượng sản phẩm mà bạn đã thêm

    # So sánh số lượng và tên sản phẩm
    assert sorted(expectedProductNames) == sorted(actualProductNames), "Tên sản phẩm không khớp"
    assert expectedQuantities == actualQuantities, "Số lượng sản phẩm không khớp"