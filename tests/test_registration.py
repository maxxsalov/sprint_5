from repos.sprint_5 import locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import re
from repos.sprint_5 import data


class TestRegistation:
    def test_registration_check_name(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(By.XPATH, locators.TestLocators.Input_name_locator).send_keys("Maxx")
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='Maxx']")))
        value = driver.find_element(By.XPATH, locators.TestLocators.Input_name_locator).get_attribute("value")
        assert value == 'Maxx'

    def test_registration_check_email(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_elements(By.XPATH, locators.TestLocators.Input_email_locator)[1].send_keys(data.mail)
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, f".//input[@value='{data.mail}']")))
        value = driver.find_elements(By.XPATH, locators.TestLocators.Input_email_locator)[1].get_attribute("value")
        assert re.match("^([*\w\.])+@([-\w]+\.)+([A-Z|a-z]{2,})", value)

    def test_registration_password_less_6_signs(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(By.XPATH, locators.TestLocators.Input_name_locator).send_keys("Maxx")
        driver.find_elements(By.XPATH, locators.TestLocators.Input_email_locator)[1].send_keys(data.mail)
        driver.find_element(By.XPATH, locators.TestLocators.Input_password_locator).send_keys("qwer")
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='qwer']")))
        driver.find_element(By.XPATH, locators.TestLocators.Log_in_locator).click()
        assert driver.find_element(By.XPATH, ".// p[text() = 'Некорректный пароль']").text == 'Некорректный пароль'


    def test_registration_successed(self, regs):
        regs.find_elements(By.XPATH, locators.TestLocators.Input_email_locator)[0].send_keys(data.mail)
        regs.find_element(By.XPATH, locators.TestLocators.Input_password_locator).send_keys(data.password)
        regs.find_element(By.XPATH, locators.TestLocators.Log_in_locator).click()
        WebDriverWait(regs, 10).until(
            expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))
        assert regs.find_element(By.XPATH, locators.TestLocators.Order_button_locator).text == "Оформить заказ"
