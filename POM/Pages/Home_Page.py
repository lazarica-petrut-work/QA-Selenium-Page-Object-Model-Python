import time

from selenium.webdriver.common.by import By
###
from POM.Locators.Home_Page_Locators import Home_Page_Locators_Class as Locator

class HomePageClass():

    def __init__(self, driver):
        self.driver = driver

        # Profile Button Objects
        self.profile_button_xpath = Locator.profile_button_xpath
        self.logout_button_linktext = Locator.logout_button_linktext
        self.about_button_linktext = Locator.about_button_linktext
        self.support_button_linktext = Locator.support_button_linktext
        self.change_password_button_linktext = Locator.change_password_button_linktext
        self.help_button_xpath = Locator.help_button_xpath

        ### Search Box
        self.search_box_xpath = Locator.search_box_xpath

        ### Page Navigation Buttons
        self.admin_button_xpath = Locator.admin_button_xpath
        self.pim_button_xpath = Locator.pim_button_xpath
        self.leave_button_xpath = Locator.leave_button_xpath
        self.time_button_xpath = Locator.time_button_xpath
        self.recruitment_button_xpath = Locator.recruitment_button_xpath
        self.my_info_button_xpath = Locator.my_info_button_xpath
        self.performance_button_xpath = Locator.performance_button_xpath
        self.dashboard_button_xpath = Locator.dashboard_button_xpath
        self.directory_button_xpath = Locator.directory_button_xpath
        self.maintenance_button_xpath = Locator.maintenance_button_xpath
        self.claim_button_xpath = Locator.claim_button_xpath
        self.buzz_button_xpath = Locator.buzz_button_xpath

    # Profile Button Objects
    def click_Profile_Button(self):
        self.driver.find_element(By.XPATH, self.profile_button_xpath).click()
    def click_Logout_Button(self):
        self.driver.find_element(By.LINK_TEXT, self.logout_button_linktext).click()
    def click_AboutButton(self):
        self.driver.find_element(By.LINK_TEXT, self.about_button_linktext).click()
    def click_SupportButton(self):
        self.driver.find_element(By.LINK_TEXT, self.support_button_linktext).click()
    def click_ChangePasswordButton(self):
        self.driver.find_element(By.LINK_TEXT, self.change_password_button_linktext).click()
    def click_HelpButton(self):
        self.driver.find_element(By.XPATH, self.help_button_xpath).click()

    ### Search Box
    def click_SearchBox(self):
        self.driver.find_element(By.XPATH, self.search_box_xpath).click()

    ### Page Navigation Buttons
    def click_AdminButton(self):
        self.driver.find_element(By.XPATH, self.admin_button_xpath).click()
    def click_PIMButton(self):
        self.driver.find_element(By.XPATH, self.pim_button_xpath).click()
    def click_LeaveButton(self):
        self.driver.find_element(By.XPATH, self.leave_button_xpath).click()
    def click_TimeButton(self):
        self.driver.find_element(By.XPATH, self.time_button_xpath).click()
    def click_RecruitmentButton(self):
        self.driver.find_element(By.XPATH, self.recruitment_button_xpath).click()
    def click_MyInfoButton(self):
        self.driver.find_element(By.XPATH, self.my_info_button_xpath).click()
    def click_PerformanceButton(self):
        self.driver.find_element(By.XPATH, self.performance_button_xpath).click()
    def click_DashboardButton(self):
        self.driver.find_element(By.XPATH, self.dashboard_button_xpath).click()
    def click_DirectoryButton(self):
        self.driver.find_element(By.XPATH, self.directory_button_xpath).click()
    def click_MaintenanceButton(self):
        self.driver.find_element(By.XPATH, self.maintenance_button_xpath).click()
    def click_ClaimsButton(self):
        self.driver.find_element(By.XPATH, self.claim_button_xpath).click()
    def click_BuzzButton(self):
        self.driver.find_element(By.XPATH, self.buzz_button_xpath).click()
