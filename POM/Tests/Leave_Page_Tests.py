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
from POM.Pages.Leave_Page import LeavePageClass


# Test Class
class LeavePageTest(unittest.TestCase):

    @classmethod
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

    def ClickLeave(self):
        home_page = HomePageClass(self.driver)
        home_page.click_LeaveButton()

    # Write Tests Down From Here

    def test_Add_Elements(self):
        leave_page = LeavePageClass(self.driver)
        self.Login()
        self.ClickLeave()
        leave_page.click_Entitlements_Dropdown()
        time.sleep(1)
        leave_page.click_Add_Entitlements_Button()
        time.sleep(1)






    # Write Tests Up From Here

    @classmethod
    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == "__main__":
    unittest.main
