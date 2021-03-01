import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formsubmission(self, getData):
        homepage = HomePage(self.driver)

        homepage.getName().send_keys(getData["FirstName"])
        homepage.getUserName().send_keys(getData["UserName"])
        homepage.getEmail().send_keys(getData["EmailId"])
        homepage.getPassword().send_keys(getData["Pwd"])

        homepage.getButton().click()
        self.selectDropDownOption(homepage.getDropDown(), "Female")

        homepage.getDropDownSelect().click()
        message = homepage.getAlertText().text
        assert "success" in message

    #@pytest.fixture(params=HomePageData.test_HomePage_data)
    #def getData(self, request):
        #return request.param

    @pytest.fixture(params=HomePageData.getTestData("TestCase2"))
    def getData(self, request):
        return request.param

