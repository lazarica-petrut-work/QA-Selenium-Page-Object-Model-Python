#Work in progress
import time
import unittest

##### Selenium
from selenium import webdriver

##### Chrome Driver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

##### Page Classes
from POM.Pages.Home_Page import HomePageClass

# Test Class
class HomePageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        ChromeService(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://opensource-demo.orangehrmlive.com/")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    # Write Tests Down From Here

    #def test_





    # Write Tests Up From Here

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main
