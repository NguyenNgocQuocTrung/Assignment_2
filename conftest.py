import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

@pytest.fixture(scope="function")  # Hoặc "session" nếu bạn muốn sử dụng driver cho toàn bộ phiên
def driver():
    PATH = 'D:/edgedriver_win64/msedgedriver.exe'
    service = Service(PATH)
    options = Options()
    driver = webdriver.Edge(service=service, options=options)
    driver.implicitly_wait(10)  # Thời gian chờ ngầm định
    yield driver
    driver.quit()  # Đảm bảo driver được đóng lại sau mỗi test


# @pytest.fixture
# def driver():
#     options = Options()
#     # WebDriverManager sẽ tự động tải và quản lý phiên bản WebDriver
#     service = Service(EdgeChromiumDriverManager().install())
#     driver = webdriver.Edge(service=service, options=options)
#     yield driver