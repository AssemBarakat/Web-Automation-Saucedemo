from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.CheckoutBTN = (By.ID, "checkout")
        self.ContinueShoppingBTN = (By.ID, "continue-shopping")
        self.RemoveBackpackatCheckout = (By.ID, "remove-sauce-labs-backpack")
        self.RemoveBikeLightatCheckout = (By.ID, "remove-sauce-labs-bike-light")
        self.RemoveBoltTshirtatCheckout = (By.ID, "remove-sauce-labs-bolt-t-shirt")
        self.RemoveFleeceJacketatCheckout = (By.ID, "remove-sauce-labs-fleece-jacket")
        self.RemoveOnesieatCheckout = (By.ID, "remove-sauce-labs-onesie")
        self.RemoveRedTshirtatCheckout = (By.ID, "remove-test.allthethings()-t-shirt-(red)")

    def click_checkout(self):
        """Clicks the checkout button to proceed to the checkout page."""
        self.driver.find_element(*self.CheckoutBTN).click()

    def click_continue_shopping(self):
        """Clicks the continue shopping button to return to the products page."""
        self.driver.find_element(*self.ContinueShoppingBTN).click()

    def remove_item(self, item_id):
        """Removes a specific item from the cart based on the given item_id."""
        item_locator = getattr(self, item_id, None)
        if item_locator:
            self.driver.find_element(*item_locator).click()
        else:
            raise ValueError(f"No item found with ID '{item_id}' to remove.")

    def remove_backpack(self):
        """Removes the backpack from the cart."""
        self.driver.find_element(*self.RemoveBackpackatCheckout).click()

    def remove_bike_light(self):
        """Removes the bike light from the cart."""
        self.driver.find_element(*self.RemoveBikeLightatCheckout).click()

    def remove_bolt_tshirt(self):
        """Removes the bolt t-shirt from the cart."""
        self.driver.find_element(*self.RemoveBoltTshirtatCheckout).click()

    def remove_fleece_jacket(self):
        """Removes the fleece jacket from the cart."""
        self.driver.find_element(*self.RemoveFleeceJacketatCheckout).click()

    def remove_onesie(self):
        """Removes the onesie from the cart."""
        self.driver.find_element(*self.RemoveOnesieatCheckout).click()

    def remove_red_tshirt(self):
        """Removes the red t-shirt from the cart."""
        self.driver.find_element(*self.RemoveRedTshirtatCheckout).click()

    def get_cart_items(self):
        """Retrieves the list of items currently in the cart."""
        return self.driver.find_elements(By.CLASS_NAME, "cart_item")


