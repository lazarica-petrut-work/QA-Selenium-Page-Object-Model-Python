

from selenium.webdriver.common.by import By

from POM.Locators.Locator_Data import LocatorsClass as Locator

class HomePageClass():

    def __init__(self, driver):
        self.driver = driver

        self.profile_button_xpath = Locator.profile_button_xpath
        self.logout_button_linktext = Locator.logout_button_linktext


    def click_Profile_Button(self):
        self.driver.find_element(By.XPATH, self.profile_button_xpath).click()

    def click_Logout_Button(self):
        self.driver.find_element(By.LINK_TEXT, self.logout_button_linktext).click()