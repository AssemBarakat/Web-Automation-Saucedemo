import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Pages.Login_Page import LoginPage
from Pages.Products_Page import ProductPage
from Pages.Cart_Page import CartPage
from Pages.Checkout_Page import CheckoutPage

@pytest.fixture(scope="function")
def setup_checkout():
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()

    # Open website and login
    login_page = LoginPage(driver)
    login_page.open("https://www.saucedemo.com")
    login_page.login("standard_user", "secret_sauce")

    # Add product to cart and navigate to checkout
    product_page = ProductPage(driver)
    product_page.interact_with_product("Backpack", "add_to_cart")
    product_page.open_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    # Yield driver for use in tests and then quit it
    yield driver
    driver.quit()

def test_complete_checkout_with_valid_data(setup_checkout):
    """TC_35: Complete checkout with valid data"""
    checkout_page = CheckoutPage(setup_checkout)
    checkout_page.fill_checkout_form("assem", "barakat", "245667")


def test_checkout_with_empty_first_name(setup_checkout):
    """TC_36: Checkout with empty first name field"""
    checkout_page = CheckoutPage(setup_checkout)
    checkout_page.fill_checkout_form("", "barakat", "245667")
    assert checkout_page.get_error_message() == "Error: First Name is required"

def test_checkout_with_empty_last_name(setup_checkout):
    """TC_37: Checkout with empty last name field"""
    checkout_page = CheckoutPage(setup_checkout)
    checkout_page.fill_checkout_form("assem", "", "245667")
    assert checkout_page.get_error_message() == "Error: Last Name is required"

def test_checkout_with_empty_zip_code(setup_checkout):
    """TC_38: Checkout with empty zip code field"""
    checkout_page = CheckoutPage(setup_checkout)
    checkout_page.fill_checkout_form("assem", "barakat", "")
    assert checkout_page.get_error_message() == "Error: Postal Code is required"

def test_checkout_with_all_fields_empty(setup_checkout):
    """TC_39: Checkout with all fields empty"""
    checkout_page = CheckoutPage(setup_checkout)
    checkout_page.fill_checkout_form("", "", "")
    assert checkout_page.get_error_message() == "Error: First Name is required"

def test_checkout_with_invalid_zip_code_format(setup_checkout):
    """TC_40: Checkout with invalid zip code format"""
    checkout_page = CheckoutPage(setup_checkout)
    checkout_page.fill_checkout_form("assem", "barakat", "abcde")
    #assert checkout_page.get_error_message() == "Error: Invalid zip code format"

def test_checkout_with_leading_trailing_spaces(setup_checkout):
    """TC_41: Checkout with leading/trailing spaces in fields"""
    checkout_page = CheckoutPage(setup_checkout)
    checkout_page.fill_checkout_form("  assem  ", "  barakat  ", "245 667")
    #assert "Thank you for your order!" in setup_checkout.page_source  # Assuming system trims spaces

def test_navigate_back_from_checkout_page(setup_checkout):
    """TC_42: Navigate back from checkout page"""
    checkout_page = CheckoutPage(setup_checkout)
    checkout_page.click_cancel()
    assert "Your Cart" in setup_checkout.page_source
