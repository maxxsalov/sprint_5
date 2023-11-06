from repos.sprint_5 import locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class TestMove:
    def test_move_to_personal_account(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        personal_button = driver.find_elements(By.XPATH, locators.TestLocators.Search_personal_button_main_locator)[0]
        personal_button.click()
        driver.get("https://stellarburgers.nomoreparties.site/login")
        email = driver.find_element(By.XPATH, locators.TestLocators.Input_email_locator).send_keys("maxx1234@yandex.ru")
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='maxx1234@yandex.ru']")))
        password = driver.find_element(By.XPATH, locators.TestLocators.Input_password_locator).send_keys("qwertyuiop")
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='qwertyuiop']")))
        driver.find_element(By.XPATH, locators.TestLocators.Log_in_locator).click()
        personal_button = driver.find_element(By.XPATH, locators.TestLocators.Search_personal_button_main_locator).click()
        driver.get("https://stellarburgers.nomoreparties.site/account/profile")
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"

    def test_move_to_constructor(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        personal_button = driver.find_elements(By.XPATH, locators.TestLocators.Search_personal_button_main_locator)[0]
        personal_button.click()
        driver.get("https://stellarburgers.nomoreparties.site/login")
        email = driver.find_element(By.XPATH, locators.TestLocators.Input_email_locator).send_keys("maxx1234@yandex.ru")
        email = driver.find_element(By.XPATH, locators.TestLocators.Input_password_locator).send_keys("qwertyuiop")
        driver.find_element(By.XPATH, locators.TestLocators.Log_in_locator).click()
        personal_button = driver.find_element(By.XPATH, locators.TestLocators.Search_personal_button_main_locator).click()
        driver.find_element(By.XPATH, locators.TestLocators.Constructor_button_locator).click()
        driver.get("https://stellarburgers.nomoreparties.site/")
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
        WebDriverWait(driver, 10)

    def test_logo_moving(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        personal_button = driver.find_elements(By.XPATH, locators.TestLocators.Search_personal_button_main_locator)[0]
        personal_button.click()
        driver.get("https://stellarburgers.nomoreparties.site/login")
        email = driver.find_element(By.XPATH, locators.TestLocators.Input_email_locator).send_keys("maxx1234@yandex.ru")
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='maxx1234@yandex.ru']")))
        password = driver.find_element(By.XPATH, locators.TestLocators.Input_password_locator).send_keys("qwertyuiop")
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='qwertyuiop']")))
        driver.find_element(By.XPATH, locators.TestLocators.Log_in_locator).click()
        personal_button = driver.find_element(By.XPATH, locators.TestLocators.Search_personal_button_main_locator).click()
        logo = driver.find_element(By.CSS_SELECTOR, locators.TestLocators.Logo_button_locator).click()
        driver.get("https://stellarburgers.nomoreparties.site/")
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
        WebDriverWait(driver, 15)
