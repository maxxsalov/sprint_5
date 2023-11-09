import pytest

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from repos.sprint_5 import locators
from repos.sprint_5 import data



@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture()
def auth(driver):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    driver.find_element(By.XPATH, locators.TestLocators.Input_email_locator).send_keys("maxx1234@yandex.ru")
    WebDriverWait(driver, 15).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='maxx1234@yandex.ru']")))
    driver.find_element(By.XPATH, locators.TestLocators.Input_password_locator).send_keys("qwertyuiop")
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='qwertyuiop']")))
    driver.find_element(By.XPATH, locators.TestLocators.Log_in_locator).click()
    return driver


@pytest.fixture()
def regs(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(By.XPATH, locators.TestLocators.Input_name_locator).send_keys(data.name)
    driver.find_elements(By.XPATH, locators.TestLocators.Input_email_locator)[1].send_keys(data.mail)
    driver.find_element(By.XPATH, locators.TestLocators.Input_password_locator).send_keys(data.password)
    driver.find_element(By.XPATH, locators.TestLocators.Log_in_locator).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/login'))
    return driver
