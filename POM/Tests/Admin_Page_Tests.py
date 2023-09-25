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
from POM.Pages.Admin_Page import AdminPageClass


# Test Class
class AdminPageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        ChromeService(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
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

    def ClickAdmin(self):
        HomePageClass.click_AdminButton()

    # Write Tests Down From Here

    #def test_
    def test_UserManagementDropdown(self):
        admin_page = AdminPageClass(self.driver)
        self.Login()
        self.ClickAdmin()
        admin_page.click_UsersManagementDropdown()





    # Write Tests Up From Here

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main
