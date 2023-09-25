from selenium.webdriver.common.by import By
###
from POM.Locators.Home_Page_Locators import Home_Page_Locators_Class as Locator

class HomePageClass():

    def __init__(self, driver):
        self.driver = driver

        self.profile_button_xpath = Locator.profile_button_xpath
        self.logout_button_linktext = Locator.logout_button_linktext
        self.admin_button_xpath = Locator.admin_button_xpath

    def click_Profile_Button(self):
        self.driver.find_element(By.XPATH, self.profile_button_xpath).click()

    def click_Logout_Button(self):
        self.driver.find_element(By.LINK_TEXT, self.logout_button_linktext).click()

    def click_AdminButton(self):
        self.driver.find_element(By.XPATH, self.admin_button_xpath).click()