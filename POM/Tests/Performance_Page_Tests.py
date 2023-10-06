import time
import unittest

##### Selenium
from selenium import webdriver

##### Chrome Driver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

##### Page Classes
from POM.Pages.Login_Page import LoginPageClass
from POM.Pages.Home_Page import HomePageClass
from POM.Pages.Performance_Page import PerformancePageClass


# Test Class
class AdminPageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        ChromeService(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://opensource-demo.orangehrmlive.com/")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)


    def Login(self):
        # Login
        login = LoginPageClass(self.driver)
        #
        login.enter_Username("Admin")
        login.enter_Password("admin123")
        #
        login.click_Login_Button()

    def ClickPerformanceButton(self):
        home_page = HomePageClass(self.driver)
        home_page.click_PerformanceButton()

    # Write Tests Down From Here

    def test_Add_Elements(self):
        recruitment_page = PerformancePageClass(self.driver)
        self.Login()
        time.sleep(1)
        self.ClickPerformanceButton()
        time.sleep(1)
        recruitment_page.click_ManageReviewsDropdown()
        time.sleep(1)
        recruitment_page.click_ManageReviewsButton()
        time.sleep(1)






    # Write Tests Up From Here

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main
