from selenium.webdriver.common.by import By
###
from POM.Locators.Admin_Page_Locators import AdminPageLocatorsClass as Locator

class AdminPageClass():

    def __init__(self, driver):
        self.driver = driver

        ### Locators
        # User Management Dropdown
        self.user_management_dropdown_xpath = Locator.user_management_dropdown_xpath
        self.users_button_linktext = Locator.users_button_linktext

        # Job Dropdown
        self.job_dropdown_xpath = Locator.job_dropdown_xpath
        self.job_titles_button_linktext = Locator.job_titles_button_linktext
        self.pay_grades_button_linktext = Locator.pay_grades_button_linktext
        self.employment_status_button_linktext = Locator.employment_status_button_linktext
        self.job_categories_button_linktext = Locator.job_categories_button_linktext
        self.work_shifts_button_linktext = Locator.work_shifts_button_linktext

        # Organization Dropdown
        self.organization_dropdown_xpath = Locator.organization_dropdown_xpath
        self.general_information_button_linktext = Locator.general_information_button_linktext
        self.locations_button_linktext = Locator.locations_button_linktext
        self.structure_button_linktext = Locator.structure_button_linktext

        # Qualifications Dropdown
        self.qualifications_dropdown_xpath = Locator.qualifications_dropdown_xpath
        self.skills_button_linktext = Locator.skills_button_linktext
        self.education_button_linktext = Locator.education_button_linktext
        self.licenses_button_linktext = Locator.licenses_button_linktext
        self.languages_button_linktext = Locator.languages_button_linktext
        self.memberships_button_linktext = Locator.memberships_button_linktext

        # Nationalities
        self.nationalities_button_linktext = Locator.nationalities_button_linktext

        # Corporate Branding
        self.corporate_branding_button_linktext = Locator.corporate_branding_button_linktext

        # Configuration Dropdown
        self.configuration_dropdown_xpath = Locator.configuration_dropdown_xpath
        self.email_configuration_button_linktext = Locator.email_configuration_button_linktext
        self.email_subscriptions_button_linktext = Locator.email_subscriptions_button_linktext
        self.localization_button_linktext = Locator.localization_button_linktext
        self.language_packages_button_linktext = Locator.language_packages_button_linktext
        self.modules_button_linktext = Locator.modules_button_linktext
        self.social_media_authentication_button_linktext = Locator.social_media_authentication_button_linktext
        self.register_oauth_client_button_linktext = Locator.register_oauth_client_button_linktext
        self.ldap_configuration_button_linktext = Locator.ldap_configuration_button_linktext

    ### Click Functions
    # User Management Dropdown
    def click_UsersManagementDropdown(self):
        self.driver.find_element(By.XPATH, self.user_management_dropdown_xpath).click()
    def click_UsersButton(self):
        self.driver.find_element(By.LINK_TEXT, self.users_button_linktext).click()

    # Job Dropdown
    def click_JobDropdown(self):
        self.driver.find_element(By.XPATH, self.job_dropdown_xpath).click()
    def click_JobTitlesButton(self):
        self.driver.find_element(By.LINK_TEXT, self.job_titles_button_linktext).click()
    def click_PayGradesButton(self):
        self.driver.find_element(By.LINK_TEXT, self.pay_grades_button_linktext).click()
    def click_EmploymentStatusButton(self):
        self.driver.find_element(By.LINK_TEXT, self.employment_status_button_linktext).click()
    def click_JobCategoriesButton(self):
        self.driver.find_element(By.LINK_TEXT, self.job_categories_button_linktext).click()
    def click_WorkShiftsButton(self):
        self.driver.find_element(By.LINK_TEXT, self.work_shifts_button_linktext).click()
    # Organization Dropdown

    def click_OrganizationDropdown(self):
        self.driver.find_element(By.XPATH, self.organization_dropdown_xpath).click()
    def click_GeneralInformationButton(self):
        self.driver.find_element(By.LINK_TEXT, self.general_information_button_linktext).click()
    def click_LocationsButton(self):
        self.driver.find_element(By.LINK_TEXT, self.locations_button_linktext).click()
    def click_StructureButton(self):
        self.driver.find_element(By.LINK_TEXT, self.structure_button_linktext).click()
    # Qualifications Dropdown

    def click_QualificationsDropdown(self):
        self.driver.find_element(By.XPATH, self.qualifications_dropdown_xpath).click()
    def click_SkillsButton(self):
        self.driver.find_element(By.LINK_TEXT, self.skills_button_linktext).click()
    def click_EducationButton(self):
        self.driver.find_element(By.LINK_TEXT, self.education_button_linktext).click()
    def click_LicensesButton(self):
        self.driver.find_element(By.LINK_TEXT, self.licenses_button_linktext).click()
    def click_LanguagesButton(self):
        self.driver.find_element(By.LINK_TEXT, self.languages_button_linktext).click()
    def click_MembershipsButton(self):
        self.driver.find_element(By.LINK_TEXT, self.memberships_button_linktext).click()
    # Nationalities

    def click_NationalitiesButton(self):
        self.driver.find_element(By.LINK_TEXT, self.nationalities_button_linktext).click()
    # Corporate Branding

    def click_CorporateBrandingButton(self):
        self.driver.find_element(By.LINK_TEXT, self.corporate_branding_button_linktext).click()

