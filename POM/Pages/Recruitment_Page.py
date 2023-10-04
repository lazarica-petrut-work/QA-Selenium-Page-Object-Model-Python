from selenium.webdriver.common.by import By
###
from POM.Locators.Recruitment_Page_Locators import RecruitmentPageLocatorsClass as Locator

class RecruitmentPageClass():

    def __init__(self, driver):
        self.driver = driver

        ### Candidates
        self.candidates_button_linktext = Locator.candidates_button_linktext

        ### Vacancies
        self.vacancies_button_linktext = Locator.vacancies_button_linktext

    ### Click Functions
    def click_CandidatesButton(self):
        self.driver.find_element(By.LINK_TEXT, self.candidates_button_linktext).click()

    def click_VacanciesButton(self):
        self.driver.find_element(By.LINK_TEXT, self.vacancies_button_linktext).click()