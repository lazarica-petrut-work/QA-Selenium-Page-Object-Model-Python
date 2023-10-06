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
from POM.Pages.PIM_Page import PIMPageClass


# Test Class
class PIMPageTest(unittest.TestCase):

    def setUp(self) -> None:
        ChromeService(ChromeDriverManager().install())
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)


    def Login(self):
        # Login
        login = LoginPageClass(self.driver)
        #
        login.enter_Username("Admin")
        login.enter_Password("admin123")
        #
        login.click_Login_Button()

    def ClickPIM(self):
        home_page = HomePageClass(self.driver)
        home_page.click_PIMButton()

    # Write Tests Down From Here

    def test_Data_Import(self):
        pim = PIMPageClass(self.driver)
        self.Login()
        self.ClickPIM()
        pim.click_ConfigurationDropdown()
        time.sleep(2)
        pim.click_DataImportButton()


    # Write Tests Up From Here

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == "__main__":
    unittest.main