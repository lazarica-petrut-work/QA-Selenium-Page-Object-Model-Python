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

# Test Class
class LoginPageTest(unittest.TestCase):

    @classmethod
    def setUp(self) -> None:
        ChromeService(ChromeDriverManager().install())
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    # Write Tests Down From Here

    def test_Login(self):
        # Login
        login = LoginPageClass(self.driver)
        ###
        login.enter_Username("Admin")
        login.enter_Password("admin123")
        time.sleep(1)
        login.click_Login_Button()

        # Delete This, Not in the Right File
        homepage = HomePageClass(self.driver)
        ###
        time.sleep(1)
        homepage.click_Profile_Button()
        time.sleep(1)
        homepage.click_Logout_Button()





    # Write Tests Up From Here

    @classmethod
    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == "__main__":
    unittest.main
