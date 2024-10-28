from selenium.webdriver.common.by import By




class LoginPage:
    def  __init__(self,driver):
        self.driver = driver
        self.username= (By.ID,"user-name")
        self.password= (By.ID,"password")
        self.login_button= (By.ID,"login-button")


    def open(self,url):
        self.driver.get(url)


    def login(self,username,password):

        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.login_button).click()