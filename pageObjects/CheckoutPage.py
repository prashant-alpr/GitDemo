from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    cardName = (By.XPATH, "div/h4/a")
    cardButton = (By.XPATH, "div/button")



    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCardName(self):
        return self.driver.find_elements(*CheckoutPage.cardName)

    def getCardButton(self):
        return self.driver.find_elements(*CheckoutPage.cardButton)

