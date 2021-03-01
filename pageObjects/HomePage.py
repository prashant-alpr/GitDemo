from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.NAME, "name")
    username = (By.CSS_SELECTOR, "input[name= 'name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    button = (By.ID, "exampleCheck1")
    dropdown = (By.ID, "exampleFormControlSelect1")
    dropdownselect = (By.XPATH, "//input[@type='submit']")
    alerttext = (By.CLASS_NAME, "alert-success")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getUserName(self):
        return self.driver.find_element(*HomePage.username)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getButton(self):
        return self.driver.find_element(*HomePage.button)

    def getDropDown(self):
        return self.driver.find_element(*HomePage.dropdown)

    def getDropDownSelect(self):
        return self.driver.find_element(*HomePage.dropdownselect)

    def getAlertText(self):
        return self.driver.find_element(*HomePage.alerttext)