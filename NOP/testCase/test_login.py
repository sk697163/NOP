from NOP.Webdrivers.webdriver_f import all_webdrivers
import unittest
from NOP.Pages.loginPage import TestLoginPage
from dotenv import load_dotenv
import os

load_dotenv()

WEB_URL = os.getenv('WEB_URL')
email,password='test1212@mailinator.com','sachin@123'


class TestLogin(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = all_webdrivers('Chrome')
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)

    #valid credential login test case
    def testLogin(self):
        driver = self.driver
        driver.get(WEB_URL)
        TestLoginPage(driver)._testLogin(email,password)

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
