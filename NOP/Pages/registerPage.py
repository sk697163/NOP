import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unittest
from selenium.common.exceptions import ElementNotInteractableException as ENIE

class TestRegisterPage(unittest.TestCase):

    def __init__(self, driver):
        self.driver = driver

    def _testRegisterPage(self, firstNameVal, lastNameVal, day, month, year, emailVal, company, passwordVal, passwordConfirmVal):
        try:
            registerButton = self.driver.find_element(
                By.CSS_SELECTOR, '.ico-register')
            registerButton.click()

            gender = self.driver.find_element(By.CSS_SELECTOR, '#gender-male')
            gender.click()

            firstname = self.driver.find_element(By.CSS_SELECTOR, '#FirstName')
            firstname.send_keys(firstNameVal)

            lastname = self.driver.find_element(By.CSS_SELECTOR, '#LastName')
            lastname.send_keys(lastNameVal)




            # select day of date of birth
            dateOfBirthDay = self.driver.find_element(
                By.XPATH, "//select[@name='DateOfBirthDay']")


            select = Select(dateOfBirthDay)
            select.select_by_visible_text(str(day))

            # select month of  birth
            dateOfBirthMonth = self.driver.find_element(
                By.CSS_SELECTOR, 'select[name="DateOfBirthMonth"]')
            select = Select(dateOfBirthMonth)
            select.select_by_visible_text(str(month))

            # select Year of  birth
            dateOfBirthYear = self.driver.find_element(
                By.CSS_SELECTOR, 'select[name="DateOfBirthYear"]')
            select = Select(dateOfBirthYear)
            select.select_by_visible_text(str(year))



            email = self.driver.find_element(By.CSS_SELECTOR, '#Email')
            email.send_keys(emailVal)

            companyName = self.driver.find_element(By.CSS_SELECTOR, '#Company')
            companyName.send_keys(company)
            time.sleep(3)
            # check weather newsletter is selected or not
            newsletter = self.driver.find_element(
                By.XPATH, '(//input[@id="Newsletter"])[1]')
            if newsletter.is_selected():
                print("Checkbox is checked")
            else:
                print("Checkbox is not checked")
            time.sleep(3)
            password = self.driver.find_element(By.CSS_SELECTOR, '#Password')
            password.send_keys(passwordVal)

            confirmPassword = self.driver.find_element(
                By.CSS_SELECTOR, '#ConfirmPassword')
            confirmPassword.send_keys(passwordConfirmVal)

            submitRegsiterd = self.driver.find_element(
                By.CSS_SELECTOR, '#register-button')

            submitRegsiterd.click()
        except  ENIE as C :
            print('Error found element is not clidkable ',C)

