from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.ContinueBTN = (By.ID, "continue")
        self.CancelBTN = (By.ID, "cancel")
        self.FirstnameField = (By.ID, "first-name")
        self.LastnameField = (By.ID, "last-name")
        self.ZipCodeField = (By.ID, "postal-code")
        self.ErrorMessage = (By.XPATH, "//*[@id='checkout_info_container']/div/form/div[1]/div[4]/h3")

    def enter_first_name(self, first_name: str):
        """Enter the first name in the checkout form."""
        first_name_field = self.driver.find_element(*self.FirstnameField)
        first_name_field.clear()
        first_name_field.send_keys(first_name)

    def enter_last_name(self, last_name: str):
        """Enter the last name in the checkout form."""
        last_name_field = self.driver.find_element(*self.LastnameField)
        last_name_field.clear()
        last_name_field.send_keys(last_name)

    def enter_zip_code(self, zip_code: str):
        """Enter the postal code in the checkout form."""
        zip_code_field = self.driver.find_element(*self.ZipCodeField)
        zip_code_field.clear()
        zip_code_field.send_keys(zip_code)

    def click_continue(self):
        """Click the continue button to proceed to the next step of checkout."""
        self.driver.find_element(*self.ContinueBTN).click()

    def click_cancel(self):
        """Click the cancel button to go back to the cart page."""
        self.driver.find_element(*self.CancelBTN).click()

    def get_error_message(self):
        """Get any displayed error message after form submission."""
        try:
            error_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.ErrorMessage)
            )
            return error_element.text
        except:
            return None

    def fill_checkout_form(self, first_name: str, last_name: str, zip_code: str):
        """Fill in the checkout form with provided details and click continue."""
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_zip_code(zip_code)
        self.click_continue()
