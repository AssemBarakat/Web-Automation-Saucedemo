import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Pages.Login_Page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def driver():
    """Set up the Chrome WebDriver and yield it for tests."""
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


accepted_password = "secret_sauce"
url = "https://www.saucedemo.com"


@pytest.mark.parametrize("username, password", [
    ("standard_user", accepted_password),
    ("locked_out_user", accepted_password),
    ("problem_user", accepted_password),
    ("performance_glitch_user", accepted_password),
    ("error_user", accepted_password),
    ("visual_user", accepted_password),
    ("assem", accepted_password),
    ("standard_user", "12345"),
    ("", accepted_password),
    ("standard_user", ""),
    ("  standard_user  ", accepted_password),
    ("STANDARD_USER", accepted_password),
    ("standard-user", accepted_password),
    ("StanDarD_UsEr", accepted_password),
    ("standard_user!", accepted_password),
    ("standard_user", "SECRET_SAUCE"),
    ("standard_user", "secret-sauce"),
    ("", "")
])
def test_login(driver, username, password):
    """Test login functionality with various username and password combinations."""
    login_page = LoginPage(driver)
    login_page.open(url)

    login_page.login(username, password)
