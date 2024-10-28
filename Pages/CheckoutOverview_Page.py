from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutFinish:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.FinishBTN = (By.ID, "finish")
        self.CancelBTN = (By.ID, "cancel")

    def click_finish(self):
        """Clicks the checkout button to proceed to the checkout page."""
        self.driver.find_element(*self.FinishBTN).click()

    def click_cancel(self):
        """Clicks the continue shopping button to return to the products page."""
        self.driver.find_element(*self.CancelBTN).click()