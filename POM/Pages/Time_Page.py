from selenium.webdriver.common.by import By
###
from POM.Locators.Time_Page_Locator import TimePageLocatorsClass as Locator

class TimePageClass():

    def __init__(self, driver):
        self.driver = driver

        ### Locators
        ### Timesheets Dropdown
        self.timesheets_dropdown_xpath = Locator.timesheets_dropdown_xpath
        #
        self.my_timesheets_button_linktext = Locator.my_timesheets_button_linktext
        self.employee_timesheets_button_linktext = Locator.employee_timesheets_button_linktext

        ### Attendance Dropdown
        self.attendance_dropdown_xpath = Locator.attendance_dropdown_xpath
        #
        self.my_records_button_linktext = Locator.my_records_button_linktext
        self.punch_in_out_button_linktext = Locator.punch_in_out_button_linktext
        self.employee_records_button_linktext = Locator.employee_records_button_linktext
        self.configuration_button_linktext = Locator.configuration_button_linktext

        ### Reports Dropdown
        self.reports_dropdown_xpath = Locator.reports_dropdown_xpath
        #
        self.project_reports_button_linktext = Locator.project_reports_button_linktext
        self.employee_reports_button_linktext = Locator.employee_reports_button_linktext
        self.attendance_summary_button_linktext = Locator.attendance_summary_button_linktext

        ### Project Info Dropdown
        self.project_info_dropdown_xpath = Locator.project_info_dropdown_xpath
        #
        self.customers_button_linktext = Locator.customers_button_linktext
        self.projects_button_linktext = Locator.projects_button_linktext


    ### Timesheets Dropdown
    def click_TimesheetsDropdown(self):
        self.driver.find_element(By.XPATH, self.timesheets_dropdown_xpath).click()
    def click_MyTimesheetsButton(self):
        self.driver.find_element(By.LINK_TEXT, self.my_timesheets_button_linktext).click()
    def click_EmployeeTimesheetsButton(self):
        self.driver.find_element(By.LINK_TEXT, self.employee_timesheets_button_linktext).click()

    ### Attendance Dropdown
    def click_AttendanceDropdown(self):
        self.driver.find_element(By.XPATH, self.attendance_dropdown_xpath).click()
    def click_MyRecordsButton(self):
        self.driver.find_element(By.LINK_TEXT, self.my_records_button_linktext).click()
    def click_PunchInOutButton(self):
        self.driver.find_element(By.LINK_TEXT, self.punch_in_out_button_linktext).click()
    def click_EmployeeRecordsButton(self):
        self.driver.find_element(By.LINK_TEXT, self.employee_records_button_linktext).click()
    def click_ConfigurationButton(self):
        self.driver.find_element(By.LINK_TEXT, self.configuration_button_linktext).click()

    ### Reports Dropdown
    def click_ReportsDropdown(self):
        self.driver.find_element(By.XPATH, self.reports_dropdown_xpath).click()
    def click_ProjectReportsButton(self):
        self.driver.find_element(By.LINK_TEXT, self.project_reports_button_linktext).click()
    def click_EmployeeReportsButton(self):
        self.driver.find_element(By.LINK_TEXT, self.employee_reports_button_linktext).click()
    def click_AttendanceSummaryButton(self):
        self.driver.find_element(By.LINK_TEXT, self.attendance_summary_button_linktext).click()

    ### Project Info Dropdown
    def click_ProjectInfoDropdown(self):
        self.driver.find_element(By.XPATH, self.project_info_dropdown_xpath).click()
    def click_CustomersButton(self):
        self.driver.find_element(By.LINK_TEXT, self.customers_button_linktext).click()
    def click_ProjectsButton(self):
        self.driver.find_element(By.LINK_TEXT, self.projects_button_linktext).click()



