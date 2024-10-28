from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

        # Locators dictionary for each product
        self.products = {
            "Backpack": {
                "add_to_cart": (By.ID, "add-to-cart-sauce-labs-backpack"),
                "remove_from_cart": (By.ID, "remove-sauce-labs-backpack"),
                "click_image": (By.XPATH, "//img[@ alt='Sauce Labs Backpack']"),
                "click_name": (By.LINK_TEXT, "Sauce Labs Backpack"),
            },
            "Bike Light": {
                "add_to_cart": (By.ID, "add-to-cart-sauce-labs-bike-light"),
                "remove_from_cart": (By.ID, "remove-sauce-labs-bike-light"),
                "click_image": (By.XPATH, "//img[@ alt='Sauce Labs Bike Light']"),
                "click_name": (By.LINK_TEXT, "Sauce Labs Bike Light"),
            },
            "Bolt T-Shirt": {
                "add_to_cart": (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
                "remove_from_cart": (By.ID, "remove-sauce-labs-bolt-t-shirt"),
                "click_image": (By.XPATH, "//img[@ alt='Sauce Labs Bolt T-Shirt']"),
                "click_name": (By.LINK_TEXT, "Sauce Labs Bolt T-Shirt"),
            },
            "Fleece Jacket": {
                "add_to_cart": (By.ID, "add-to-cart-sauce-labs-fleece-jacket"),
                "remove_from_cart": (By.ID, "remove-sauce-labs-fleece-jacket"),
                "click_image": (By.XPATH, "//img[@ alt='Sauce Labs Fleece Jacket']"),
                "click_name": (By.LINK_TEXT, "Sauce Labs Fleece Jacket"),
            },
            "Onesie": {
                "add_to_cart": (By.ID, "add-to-cart-sauce-labs-onesie"),
                "remove_from_cart": (By.ID, "remove-sauce-labs-onesie"),
                "click_image": (By.XPATH, "//img[@ alt='Sauce Labs Onesie']"),
                "click_name": (By.LINK_TEXT, "Sauce Labs Onesie"),
            },
            "Red T-Shirt": {
                "add_to_cart": (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)"),
                "remove_from_cart": (By.ID, "remove-test.allthethings()-t-shirt-(red)"),
                "click_image": (By.XPATH, "//img[@ alt='Test.allTheThings() T-Shirt (Red)']"),
                "click_name": (By.LINK_TEXT, "Test.allTheThings() T-Shirt (Red)"),
            }
        }

        # Cart Icon
        self.CartIcon = (By.ID, "shopping_cart_container")

        # Filter Dropdown
        self.FilterDropdown = (By.CLASS_NAME, "product_sort_container")

    def interact_with_product(self, product_name, action):
        """
        Interact with a specific product by name and action type.
        :param product_name: Name of the product (e.g., "Backpack", "Bike Light").
        :param action: Action to perform (e.g., "add_to_cart", "remove_from_cart", "click_image", "click_name").
        """
        locator = self.products[product_name][action]
        self.driver.find_element(*locator).click()

    def select_filter_option(self, option_text):
        """Select a filter option from the dropdown by visible text."""
        filter_dropdown = Select(self.driver.find_element(*self.FilterDropdown))
        filter_dropdown.select_by_visible_text(option_text)

    def open_cart(self):
        """Click on the cart icon to open the cart page."""
        self.driver.find_element(*self.CartIcon).click()


