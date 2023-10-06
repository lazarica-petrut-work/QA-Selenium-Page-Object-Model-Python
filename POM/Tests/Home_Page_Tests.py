#Work in progress
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
class HomePageTest(unittest.TestCase):


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

    # Write Tests Down From Here

    def test_Homebutton(self):
        home_page = HomePageClass(self.driver)
        self.Login()
        time.sleep(2)
        home_page.click_AdminButton()
        time.sleep(2)

    def test_log_out(self):
        home_page = HomePageClass(self.driver)
        self.Login()
        time.sleep(1)
        home_page.click_Profile_Button()
        time.sleep(2)
        home_page.click_Logout_Button()
        time.sleep(2)

    # Write Tests Up From Here


    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == "__main__":
    unittest.main
