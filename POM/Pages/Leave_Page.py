from selenium.webdriver.common.by import By
###
from POM.Locators.Leave_Page_Locators import Leave_Page_Locators_Class as Locator

class LeavePageClass():

    def __init__(self, driver):
        self.driver = driver

        ### Locators
        # Apply
        self.apply_button_linktext = Locator.apply_button_linktext

        # My Leave
        self.my_leave_button_linktext = Locator.my_leave_button_linktext

        # Entitlements Dropdown
        self.entitlements_dropdown_xpath = Locator.entitlements_dropdown_xpath
        #
        self.add_entitlements_button_linktext = Locator.add_entitlements_button_linktext
        self.employee_entitlements_button_linktext = Locator.employee_entitlements_button_linktext
        self.my_entitlements_button_linktext = Locator.my_entitlements_button_linktext

        # Reports Dropdown
        self.reports_dropdown_xpath = Locator.reports_dropdown_xpath
        #
        self.leave_entitlements_and_usage_report_button_linktext = Locator.leave_entitlements_and_usage_report_button_linktext
        self.my_leave_entitlements_and_usage_report_button_linktext = Locator.my_leave_entitlements_and_usage_report_button_linktext

        # Configure Dropdown
        self.configure_dropdown_xpath = Locator.configure_dropdown_xpath
        self.leave_period_button_linktext = Locator.leave_period_button_linktext
        self.leave_types_button_linktext = Locator.leave_types_button_linktext
        self.work_week_button_linktext = Locator.work_week_button_linktext
        self.holidays_button_linktext = Locator.holidays_button_linktext

        # Leave List
        self.leave_list_button_linktext = Locator.leave_list_button_linktext

        # Assign Leave
        self.assign_leave_button_linktext = Locator.assign_leave_button_linktext

    ### Click Functions
    # Apply
    def click_Apply_Button(self):
        self.driver.find_element(By.LINK_TEXT, self.apply_button_linktext).click()

    # My Leave
    def click_My_Leave_Button(self):
        self.driver.find_element(By.LINK_TEXT, self.my_leave_button_linktext).click()

    # Entitlements Dropdown
    def click_Entitlements_Dropdown(self):
        self.driver.find_element(By.XPATH, self.entitlements_dropdown_xpath).click()
    #
    def click_Add_Entitlements_Button(self):
        self.driver.find_element(By.LINK_TEXT, self.add_entitlements_button_linktext).click()
    def click_Employee_Entitlements_Button(self):
        self.driver.find_element(By.LINK_TEXT, self.employee_entitlements_button_linktext).click()
    def click_My_Entitlements_Button(self):
        self.driver.find_element(By.LINK_TEXT, self.my_entitlements_button_linktext).click()

    # Reports Dropdown
    def click_Reports_Dropdown(self):
        self.driver.find_element(By.XPATH, self.reports_dropdown_xpath).click()
    #
    def click_Leave_Entitlements_And_Usage_Report_Button(self):
        self.driver.find_element(By.LINK_TEXT, self.leave_entitlements_and_usage_report_button_linktext).click()
    def click_My_Leave_Entitlements_And_Usage_Report_Button(self):
        self.driver.find_element(By.LINK_TEXT, self.my_leave_entitlements_and_usage_report_button_linktext).click()

    # Configure Dropdown
    def click_Configure_Dropdown(self):
        self.driver.find_element(By.XPATH, self.configure_dropdown_xpath).click()
    #
    def click_Leave_Period_Button(self):
        self.driver.find_element(By.LINK_TEXT, self.leave_period_button_linktext).click()
    def click_Leave_Types_Button(self):
        self.driver.find_element(By.LINK_TEXT, self.leave_types_button_linktext).click()
    def click_Work_Week_Button(self):
        self.driver.find_element(By.LINK_TEXT, self.work_week_button_linktext).click()
    def click_Holidays_Button(self):
        self.driver.find_element(By.LINK_TEXT, self.holidays_button_linktext).click()

    # Leave List
    def click_Leave_List_Button(self):
        self.driver.find_element(By.LINK_TEXT, self.leave_list_button_linktext).click()

    # Assign Leave
    def click_Assign_Leave_Button(self):
        self.driver.find_element(By.LINK_TEXT, self.assign_leave_button_linktext).click()
