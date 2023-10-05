from selenium.webdriver.common.by import By
###
from POM.Locators.My_Info_Page_Locators import MyInfoPageLocatorsClass as Locator

class MyInfoPageClass():

    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.personal_details_button_linktext = Locator.personal_details_button_linktext
        self.contact_details_button_linktext = Locator.contact_details_button_linktext
        self.emergency_contacts_button_linktext = Locator.emergency_contacts_button_linktext
        self.dependents_button_linktext = Locator.dependents_button_linktext
        self.immigration_button_linktext = Locator.immigration_button_linktext
        self.job_button_linktext = Locator.job_button_linktext
        self.salary_button_linktext = Locator.salary_button_linktext
        self.tax_exemptions_button_linktext = Locator.tax_exemptions_button_linktext
        self.report_to_button_linktext = Locator.report_to_button_linktext
        self.qualifications_button_linktext = Locator.qualifications_button_linktext
        self.memberships_button_linktext = Locator.memberships_button_linktext

    ### Click Functions
    def click_PersonalDetailsButton(self):
        self.driver.find_element(By.LINK_TEXT, self.personal_details_button_linktext).click()

    def click_ContactDetailsButton(self):
        self.driver.find_element(By.LINK_TEXT, self.contact_details_button_linktext).click()

    def click_EmergencyContactsButton(self):
        self.driver.find_element(By.LINK_TEXT, self.emergency_contacts_button_linktext).click()

    def click_DependentsButton(self):
        self.driver.find_element(By.LINK_TEXT, self.dependents_button_linktext).click()

    def click_ImmigrationButton(self):
        self.driver.find_element(By.LINK_TEXT, self.immigration_button_linktext).click()

    def click_JobButton(self):
        self.driver.find_element(By.LINK_TEXT, self.job_button_linktext).click()

    def click_SalaryButton(self):
        self.driver.find_element(By.LINK_TEXT, self.salary_button_linktext).click()

    def click_TaxExemptionsButton(self):
        self.driver.find_element(By.LINK_TEXT, self.tax_exemptions_button_linktext).click()

    def click_ReportToButton(self):
        self.driver.find_element(By.LINK_TEXT, self.report_to_button_linktext).click()

    def click_QualificationsButton(self):
        self.driver.find_element(By.LINK_TEXT, self.qualifications_button_linktext).click()

    def click_MembershipsButton(self):
        self.driver.find_element(By.LINK_TEXT, self.memberships_button_linktext).click()

