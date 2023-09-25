from selenium import  webdriver
from selenium.webdriver.common.by import By

from POM.Locators.Login_Page_Locators import Login_Page_Locators_Class as Locator

class LoginPageClass():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_xpath = Locator.username_textbox_xpath
        self.password_textbox_xpath = Locator.password_textbox_xpath
        self.login_button_xpath = Locator.login_button_xpath


    def enter_Username(self, username):
        self.driver.find_element(By.XPATH, self.username_textbox_xpath).clear
        self.driver.find_element(By.XPATH, self.username_textbox_xpath).send_keys(username)

    def enter_Password(self, password):
        self.driver.find_element(By.XPATH, self.password_textbox_xpath).clear
        self.driver.find_element(By.XPATH, self.password_textbox_xpath).send_keys(password)

    def click_Login_Button(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()