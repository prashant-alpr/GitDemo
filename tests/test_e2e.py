from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        homePage.shopItems()
        log.info("getting all the card titles")
        checkoutPage = CheckoutPage(self.driver)
        cards = checkoutPage.getCardTitles()
        cardName = checkoutPage.getCardName()
        cardButton = checkoutPage.getCardButton()

        for card in cards:
            productName = card.text
            log.info(productName)
            if productName == "Blackberry":
                cardButton.click()

        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        log.info("Entering country name as ind")
        self.driver.find_element_by_id("country").send_keys("ind")
        self.verifyLinkPresence("India")
        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("input[type='submit']").click()
        success = self.driver.find_element_by_class_name("alert-success").text
        log.info("Text received from application is" + success)
        assert "Success! Thank you!" in success

        self.driver.get_screenshot_as_file("screen.png")
