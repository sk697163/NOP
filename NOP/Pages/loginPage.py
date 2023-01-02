import time
import unittest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class TestLoginPage(unittest.TestCase):

    def __init__(self,driver):
        self.driver=driver

    def _testLogin(self,email,password):

        loginButton=self.driver.find_element(By.CSS_SELECTOR,'.ico-login')
        loginButton.click()

        inputEmail=self.driver.find_element(By.CSS_SELECTOR,'#Email')
        inputEmail.send_keys(email)

        inputPassword = self.driver.find_element(By.CSS_SELECTOR, '#Password')
        inputPassword.send_keys(password)

        remeber=self.driver.find_element(By.CSS_SELECTOR,'#RememberMe')
        result=remeber.is_selected()

        if result:
            print('this is already selected')
        else:
            remeber.click()
            print('remember is selected')


        login=self.driver.find_element(By.XPATH, '#//button[normalize-space()="Log in"]')
        login.click()
        time.sleep(5)

        try :
            noAccountFound=self.driver.find_element(By.XPATH,"//div[@class='message-error validation-summary-errors']").getText()
            assert noAccountFound=='Login was unsuccessful. Please correct the errors and try again.'
            print('noAccountFound',noAccountFound)
        except NoSuchElementException as e:
            print("user not found",e)
