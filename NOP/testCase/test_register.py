from NOP.Webdrivers import webdriver_f
from dotenv import load_dotenv
from NOP.Pages.registerPage import TestRegisterPage
import os
import unittest
import sys
sys.path.append("/Users/mac/apps/NOPEcommerce/NOP/testCase")


load_dotenv()

# Load varibale from environment button
WEB_URL = os.getenv('WEB_URL')
firstNameVal, lastNameVal, day, month, year, emailVal, company, passwordVal, passwordConfirmVal = 'sachin', 'kumar', 3, 'March', 1999, 'test1212@mailinator.com', 'credit', 'sachin@123', 'sachin@123'
invalidemailVal='test.com'

class TestRegister(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver_f.all_webdrivers('Chrome')
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)

    #Valid details test case
    @unittest.skip("i have checked this one ")
    def test_register_case(self):
        driver = self.driver
        driver.get(WEB_URL)
        TestRegisterPage(driver)._testRegisterPage(firstNameVal, lastNameVal,
                                                   day, month, year, emailVal,
                                                   company, passwordVal,
                                                   passwordConfirmVal)
    # inValid email test case
    def test_register_case(self):
        driver = self.driver
        driver.get(WEB_URL)
        TestRegisterPage(driver)._testRegisterPage(firstNameVal, lastNameVal,
                                                   day, month, year, invalidemailVal,
                                                   company, passwordVal,
                                                   passwordConfirmVal)

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
