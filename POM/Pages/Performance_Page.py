from selenium.webdriver.common.by import By
###
from POM.Locators.Performance_Page_Locators import PerformancePageLocatorsClass as Locator

class PerformancePageClass():

    def __init__(self, driver):
        self.driver = driver

        ### Configure Dropdown
        self.configure_dropdown_xpath = Locator.configure_dropdown_xpath
        #
        self.kpis_button_linktext = Locator.kpis_button_linktext
        self.trackers_button_linktext = Locator.trackers_button_linktext

        ### Manage Reviews Dropdown
        self.manage_reviews_dropdown_xpath = Locator.manage_reviews_dropdown_xpath
        #
        self.manage_reviews_button_linktext = Locator.manage_reviews_button_linktext
        self.my_reviews_button_linktext = Locator.my_reviews_button_linktext
        self.employee_reviews_button_linktext = Locator.employee_reviews_button_linktext

        # My Trackers
        self.my_trackers_button_linktext = Locator.my_trackers_button_linktext

        # Employee Trackers
        self.employee_trackers_button_linktext = Locator.employee_trackers_button_linktext

    ### Click Functions
    #@ Configure Dropdown
    def click_ConfigureDropdown(self):
        self.driver.find_element(By.XPATH, self.configure_dropdown_xpath).click()
    #
    def click_KPIsButton(self):
        self.driver.find_element(By.LINK_TEXT, self.kpis_button_linktext).click()
    def click_TrackersButton(self):
        self.driver.find_element(By.LINK_TEXT, self.trackers_button_linktext).click()

    ## Manage Reviews Dropdown
    def click_ManageReviewsDropdown(self):
        self.driver.find_element(By.XPATH, self.manage_reviews_dropdown_xpath).click()
    #
    def click_ManageReviewsButton(self):
        self.driver.find_element(By.LINK_TEXT, self.manage_reviews_button_linktext).click()
    def click_MyReviewsButton(self):
        self.driver.find_element(By.LINK_TEXT, self.my_reviews_button_linktext).click()
    def click_EmployeeReviewsButton(self):
        self.driver.find_element(By.LINK_TEXT, self.employee_reviews_button_linktext).click()

    # My Trackers
    def click_MyTrackersButton(self):
        self.driver.find_element(By.LINK_TEXT, self.my_trackers_button_linktext).click()

    # Employee Trackers
    def click_EmployeeTrackersButton(self):
        self.driver.find_element(By.LINK_TEXT, self.employee_trackers_button_linktext).click()
