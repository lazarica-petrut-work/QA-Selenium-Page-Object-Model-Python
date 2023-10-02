from selenium.webdriver.common.by import By
###
from POM.Locators.PIM_Page_Locators import PIM_Page_Locators_Class as Locator

class PIMPageClass():

    def __init__(self, driver):
        self.driver = driver

        ### Locators
        # Configuration Dropdown
        self.configuration_dropdown_xpath = Locator.configuration_dropdown_xpath
        self.optional_fields_button_linktext = Locator.optional_fields_button_linktext
        self.custom_fields_button_linktext = Locator.custom_fields_button_linktext
        self.data_import_button_linktext = Locator.data_import_button_linktext
        self.reporting_methods_button_linktext = Locator.reporting_methods_button_linktext
        self.termination_reasons_button_linktext = Locator.termination_reasons_button_linktext

        # Employee List
        self.employee_list_button_linktext = Locator.employee_list_button_linktext

        # Add Employee
        self.add_employee_button_linktext = Locator.add_employee_button_linktext

        # Reports
        self.reports_button_linktext = Locator.reports_button_linktext

    ### Click Functions
    # Configuration Dropdown
    def click_ConfigurationDropdown(self):
        self.driver.find_element(By.XPATH, self.configuration_dropdown_xpath).click()
    def click_OptionalFieldsButton(self):
        self.driver.find_element(By.LINK_TEXT, self.optional_fields_button_linktext).click()
    def click_CustomFieldsButton(self):
        self.driver.find_element(By.LINK_TEXT, self.custom_fields_button_linktext).click()
    def click_DataImportButton(self):
        self.driver.find_element(By.LINK_TEXT, self.data_import_button_linktext).click()
    def click_ReportingMethodsButton(self):
        self.driver.find_element(By.LINK_TEXT, self.reporting_methods_button_linktext).click()
    def click_TerminationReasonsButton(self):
        self.driver.find_element(By.LINK_TEXT, self.termination_reasons_button_linktext).click()
    def click_EmployeeListButton(self):
        self.driver.find_element(By.LINK_TEXT, self.employee_list_button_linktext).click()
    def click_AddEmployeeButton(self):
        self.driver.find_element(By.LINK_TEXT, self.add_employee_button_linktext).click()
    def click_ReportsButton(self):
        self.driver.find_element(By.LINK_TEXT, self.reports_button_linktext).click()
