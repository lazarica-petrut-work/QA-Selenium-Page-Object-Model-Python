import unittest
#HTML Report
from HTMLTestRunner.runner import HTMLTestRunner

# Import Test Classes Here
from POM.Tests.Login_Page_Tests import LoginPageTest
from POM.Tests.Home_Page_Tests import HomePageTest
from POM.Tests.Admin_Page_Tests import AdminPageTest


# Test Suit Class
class TestingClass(unittest.TestCase):

    # Test Suit
    def test_suit(self):
        my_test_suit = unittest.TestSuite()
        my_test_suit.addTests([
            # Add Imported Test Classes Here
            unittest.defaultTestLoader.loadTestsFromTestCase(LoginPageTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(HomePageTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(AdminPageTest),
        ])

        # Test Runner HTML Report
        my_test_runner = HTMLTestRunner(
            output = "report",
            title = "Test report",
            report_name = "report",
            tested_by = "Lazarica Petrut"
        )

        my_test_runner.run(my_test_suit)

if __name__ == "__main__":
    unittest.main()