import time
import unittest

##### Selenium
from selenium import  webdriver

##### Chrome Driver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

##### Classes
from POM.Pages.Login_Page import LoginPageClass
from POM.Pages.Home_Page import HomePageClass




class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        ChromeService(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://opensource-demo.orangehrmlive.com/")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_Login(self):
        driver = self.driver
        login = LoginPageClass(driver)
        login.enter_Username("Admin")
        login.enter_Password("admin123")
        time.sleep(1)
        login.click_Login_Button()

        homepage = HomePageClass(driver)
        time.sleep(1)
        homepage.click_Profile_Button()
        time.sleep(1)
        homepage.click_Logout_Button()



    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main



