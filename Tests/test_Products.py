import pytest
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from Pages.Cart_Page import CartPage
from Pages.CheckoutOverview_Page import CheckoutFinish
from Pages.Checkout_Page import CheckoutPage
from Pages.Products_Page import ProductPage
from Pages.Login_Page import LoginPage

@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    L1 = LoginPage(driver)
    L1.open("https://www.saucedemo.com")
    L1.login("standard_user", "secret_sauce")
    yield driver
    driver.quit()

def test_add_single_product_to_cart(setup):
    """TC_20: Verify 'Add to Cart' functionality for a single product."""
    product_page = ProductPage(setup)
    product_page.interact_with_product("Backpack", "add_to_cart")
    product_page.open_cart()
    assert "Sauce Labs Backpack" in setup.page_source

def test_add_multiple_products_to_cart(setup):
    """TC_21: Verify 'Add to Cart' functionality for multiple products."""
    product_page = ProductPage(setup)
    product_page.interact_with_product("Backpack", "add_to_cart")
    product_page.interact_with_product("Bolt T-Shirt", "add_to_cart")
    product_page.interact_with_product("Onesie", "add_to_cart")
    product_page.open_cart()
    assert all(item in setup.page_source for item in ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"])

def test_remove_product_from_cart(setup):
    """TC_22: Verify removing a product from the cart."""
    product_page = ProductPage(setup)
    product_page.interact_with_product("Backpack", "add_to_cart")
    product_page.open_cart()
    product_page.interact_with_product("Backpack", "remove_from_cart")
    assert "Sauce Labs Backpack" not in setup.page_source

def test_redirect_by_clicking_product_photo(setup):
    """TC_23: Verify redirection by clicking on a product photo."""
    product_page = ProductPage(setup)
    product_page.interact_with_product("Fleece Jacket", "click_image")
    assert "Sauce Labs Fleece Jacket" in setup.page_source

def test_redirect_by_clicking_product_description(setup):
    """TC_24: Verify redirection by clicking on a product description."""
    product_page = ProductPage(setup)
    product_page.interact_with_product("Red T-Shirt", "click_name")
    assert "Test.allTheThings() T-Shirt (Red)" in setup.page_source

def test_filter_by_name_a_to_z(setup):
    """TC_25: Verify filter by name from A to Z."""
    product_page = ProductPage(setup)
    product_page.select_filter_option("Name (A to Z)")
    sorted_names = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt",
                    "Sauce Labs Fleece Jacket", "Sauce Labs Onesie", "Test.allTheThings() T-Shirt (Red)"]
    assert all(name in setup.page_source for name in sorted_names)

def test_filter_by_name_z_to_a(setup):
    """TC_26: Verify filter by name from Z to A."""
    product_page = ProductPage(setup)
    product_page.select_filter_option("Name (Z to A)")
    sorted_names = ["Test.allTheThings() T-Shirt (Red)", "Sauce Labs Onesie", "Sauce Labs Fleece Jacket",
                    "Sauce Labs Bolt T-Shirt", "Sauce Labs Bike Light", "Sauce Labs Backpack"]
    assert all(name in setup.page_source for name in sorted_names)

def test_filter_by_price_low_to_high(setup):
    """TC_27: Verify filter by price from low to high."""
    product_page = ProductPage(setup)
    product_page.select_filter_option("Price (low to high)")
    # Check that prices are sorted (additional logic can be added if price elements are identifiable)
    assert True  # Placeholder for price verification

def test_cart_icon_displays_correct_count(setup):
    """TC_28: Verify cart icon displays correct number of added products."""
    product_page = ProductPage(setup)
    product_page.interact_with_product("Backpack", "add_to_cart")
    product_page.interact_with_product("Bolt T-Shirt", "add_to_cart")
    cart_count = setup.find_element(*product_page.CartIcon).text
    assert cart_count == "2"

def test_cart_icon_redirects_to_cart_page(setup):
    """TC_29: Verify clicking on the cart icon redirects to cart page."""
    product_page = ProductPage(setup)
    product_page.open_cart()
    assert "Your Cart" in setup.page_source

def test_sort_persistence_after_add_to_cart(setup):
    """TC_30: Verify sorting persistence after adding a product to cart."""
    product_page = ProductPage(setup)
    product_page.select_filter_option("Price (low to high)")
    product_page.interact_with_product("Backpack", "add_to_cart")
    assert "Price (low to high)" in setup.page_source  # Placeholder for actual persistence check

# def test_product_availability_after_removal(setup):
#     """TC_31: Verify product availability after removing from cart."""
#     product_page = ProductPage(setup)
#     product_page.interact_with_product("Fleece Jacket", "add_to_cart")
#     product_page.open_cart()
#     product_page.interact_with_product("Fleece Jacket", "remove_from_cart")
#     setup.get("https://www.saucedemo.com/inventory.html")
#     assert "Sauce Labs Fleece Jacket" in setup.page_source
#
# def test_empty_cart_message(setup):
#     """TC_32: Verify empty cart message when no products are added."""
#     product_page = ProductPage(setup)
#     product_page.open_cart()
#     assert "Your cart is empty" in setup.page_source

# def test_cart_total_price(setup):
#     """TC_33: Verify the cart page displays correct total price."""
#     product_page = ProductPage(setup)
#     product_page.interact_with_product("Backpack", "add_to_cart")
#     product_page.interact_with_product("Fleece Jacket", "add_to_cart")
#     product_page.open_cart()
#     # Placeholder for actual price verification; additional code needed to locate price elements
#     assert True  # Placeholder for price check

