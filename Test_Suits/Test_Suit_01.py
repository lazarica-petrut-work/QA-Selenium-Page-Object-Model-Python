import unittest
#HTML Report
from HTMLTestRunner.runner import HTMLTestRunner

# Import Test Classes Here
from POM.Tests.Login_Page_Tests import LoginPageTest
from POM.Tests.Home_Page_Tests import HomePageTest
from POM.Tests.Admin_Page_Tests import AdminPageTest
from POM.Tests.Leave_Page_Tests import LeavePageTest
from POM.Tests.My_Info_Page_Tests import MyInfoPageTest
from POM.Tests.Performance_Page_Tests import PerformancePageTest
from POM.Tests.PIM_Page_Tests import PIMPageTest
from POM.Tests.Recruitment_Page_Tests import RecruitmentPageTest
from POM.Tests.Time_Page_Tests import TimePageTest

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
            unittest.defaultTestLoader.loadTestsFromTestCase(LeavePageTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(MyInfoPageTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(PerformancePageTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(PIMPageTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(RecruitmentPageTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(TimePageTest)

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