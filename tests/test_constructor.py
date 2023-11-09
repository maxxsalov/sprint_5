from repos.sprint_5 import locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class TestConstructor:
    def test_constructor_transfer_to_fillings(self, auth):
        auth.find_element(By.XPATH, locators.TestLocators.Constructor_button_locator).click()
        WebDriverWait(auth, 10).until(
            expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/"))
        auth.find_element(By.XPATH, locators.TestLocators.Fillings_tab_locator).click()
        auth.implicitly_wait(10)
        auth.find_element(By.XPATH, locators.TestLocators.Example_fillings_locator).click()
        WebDriverWait(auth, 10).until(
            expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/ingredient/61c0c5a71d1f82001bdaaa6f'))
        assert auth.current_url == 'https://stellarburgers.nomoreparties.site/ingredient/61c0c5a71d1f82001bdaaa6f'

    def test_constructor_transfer_to_sauce(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, locators.TestLocators.Sauce_tab_locator).click()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, locators.TestLocators.Example_sauce_locator).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.url_to_be(
                'https://stellarburgers.nomoreparties.site/ingredient/61c0c5a71d1f82001bdaaa73'))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/ingredient/61c0c5a71d1f82001bdaaa73'

    def test_constructor_transfer_to_buns(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, locators.TestLocators.Sauce_tab_locator).click()
        driver.find_element(By.XPATH, locators.TestLocators.Buns_tab_locator).click()
        driver.find_element(By.XPATH, locators.TestLocators.Example_buns_locator).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.url_to_be(
                'https://stellarburgers.nomoreparties.site/ingredient/61c0c5a71d1f82001bdaaa6d'))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/ingredient/61c0c5a71d1f82001bdaaa6d'