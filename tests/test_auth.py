from repos.sprint_5 import locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class TestAuthorization:

    def test_authorization_the_private_account(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_elements(By.XPATH, locators.TestLocators.Search_personal_button_main_locator)[0].click()
        WebDriverWait(driver, 10).until(
            expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        driver.find_elements(By.XPATH, locators.TestLocators.Input_email_locator)[0].send_keys("maxx1234@yandex.ru")
        WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='maxx1234@yandex.ru']")))
        driver.find_element(By.XPATH, locators.TestLocators.Input_password_locator).send_keys("qwertyuiop")
        WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='qwertyuiop']")))
        driver.find_element(By.XPATH, locators.TestLocators.Log_in_locator).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert driver.find_element(By.XPATH, locators.TestLocators.Order_button_locator).text == "Оформить заказ"

    def test_authorization_in_the_system(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, locators.TestLocators.Search_button_main_locator).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        driver.find_elements(By.XPATH, locators.TestLocators.Input_email_locator)[0].send_keys("maxx1234@yandex.ru")
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='maxx1234@yandex.ru']")))
        driver.find_element(By.XPATH, locators.TestLocators.Input_password_locator).send_keys("qwertyuiop")
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='qwertyuiop']")))
        driver.find_element(By.XPATH, locators.TestLocators.Log_in_locator).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert driver.find_element(By.XPATH, locators.TestLocators.Order_button_locator).text == "Оформить заказ"

    def test_authorization_via_recovery_form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(By.XPATH, locators.TestLocators.Recover_password_locator).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/forgot-password"))
        driver.find_element(By.XPATH, locators.TestLocators.Input_email_locator).send_keys("maxx1234@yandex.ru")
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='maxx1234@yandex.ru']")))
        driver.find_element(By.XPATH, locators.TestLocators.Recovery_button_locator).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/reset-password"))
        driver.find_element(By.XPATH, locators.TestLocators.Login_button_locator).click()
        driver.find_element(By.XPATH, locators.TestLocators.Input_email_locator).send_keys("maxx1234@yandex.ru")
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='maxx1234@yandex.ru']")))
        driver.find_element(By.XPATH, locators.TestLocators.Input_password_locator).send_keys("qwertyuiop")
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='qwertyuiop']")))
        driver.find_element(By.XPATH, locators.TestLocators.Log_in_locator).click()
        WebDriverWait(driver, 15).until(
            expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert driver.find_element(By.XPATH, locators.TestLocators.Order_button_locator).text == "Оформить заказ"

    def test_logout_from_account(self, auth):
        auth.find_element(By.XPATH, locators.TestLocators.Search_personal_button_main_locator).click()
        auth.implicitly_wait(10)
        auth.find_element(By.XPATH, locators.TestLocators.Logout_button_locator).click()
        WebDriverWait(auth, 10).until(
            expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        assert auth.find_element(By.XPATH, locators.TestLocators.Log_in_locator).text == 'Войти'
