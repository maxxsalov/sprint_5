from repos.sprint_5 import locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class TestConstructor:
    def test_constructor_transfer_to_fillings(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        personal_button = driver.find_elements(By.XPATH, locators.TestLocators.Search_personal_button_main_locator)[0]
        personal_button.click()
        driver.get("https://stellarburgers.nomoreparties.site/login")
        email = driver.find_element(By.XPATH, locators.TestLocators.Input_email_locator).send_keys("maxx1234@yandex.ru")
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='maxx1234@yandex.ru']")))
        password = driver.find_element(By.XPATH, locators.TestLocators.Input_password_locator).send_keys("qwertyuiop")
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='qwertyuiop']")))
        driver.find_element(By.XPATH, locators.TestLocators.Log_in_locator).click()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, locators.TestLocators.Fillings_tab_locator).click()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, locators.TestLocators.Example_fillings_locator).click()
        driver.get('https://stellarburgers.nomoreparties.site/ingredient/61c0c5a71d1f82001bdaaa6f')
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/ingredient/61c0c5a71d1f82001bdaaa6f'

    def test_constructor_transfer_to_sauce(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, locators.TestLocators.Sauce_tab_locator).click()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, locators.TestLocators.Example_sauce_locator).click()
        driver.get('https://stellarburgers.nomoreparties.site/ingredient/61c0c5a71d1f82001bdaaa73')
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/ingredient/61c0c5a71d1f82001bdaaa73'

    def test_constructor_transfer_to_buns(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, locators.TestLocators.Sauce_tab_locator).click()
        driver.find_element(By.XPATH, locators.TestLocators.Buns_tab_locator).click()
        driver.find_element(By.XPATH, locators.TestLocators.Example_buns_locator).click()
        driver.get('https://stellarburgers.nomoreparties.site/ingredient/61c0c5a71d1f82001bdaaa6d')
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/ingredient/61c0c5a71d1f82001bdaaa6d'