from repos.sprint_5 import locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class TestAuthorization:
    def test_authorization_the_registration_form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        name = driver.find_element(By.XPATH, locators.TestLocators.Input_name_locator).send_keys("Maxx")
        email = driver.find_elements(By.XPATH, locators.TestLocators.Input_email_locator)[1]
        email.send_keys("maxx1234@yandex.ru")
        password = driver.find_element(By.XPATH, locators.TestLocators.Input_password_locator).send_keys("qwertyuiop")
        driver.find_element(By.XPATH, locators.TestLocators.Log_in_locator).click()
        driver.get("https://stellarburgers.nomoreparties.site/login")
        email = driver.find_element(By.XPATH, locators.TestLocators.Input_email_locator).send_keys("maxx1234@yandex.ru")
        password = driver.find_element(By.XPATH, locators.TestLocators.Input_password_locator).send_keys("qwerty")
        driver.find_element(By.XPATH, locators.TestLocators.Log_in_locator).click()
        driver.get("https://stellarburgers.nomoreparties.site/")
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
        WebDriverWait(driver, 10)

    def test_authorization_the_private_account(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        personal_button = driver.find_elements(By.XPATH, locators.TestLocators.Search_personal_button_main_locator)[0]
        personal_button.click()
        driver.get("https://stellarburgers.nomoreparties.site/login")
        email = driver.find_element(By.XPATH, locators.TestLocators.Input_email_locator).send_keys("maxx1234@yandex.ru")
        WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='maxx1234@yandex.ru']")))
        password = driver.find_element(By.XPATH, locators.TestLocators.Input_password_locator).send_keys("qwertyuiop")
        WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='qwertyuiop']")))
        driver.find_element(By.XPATH, locators.TestLocators.Log_in_locator).click()
        driver.get("https://stellarburgers.nomoreparties.site/")
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_authorization_in_the_system(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, locators.TestLocators.Search_button_main_locator).click()
        driver.get("https://stellarburgers.nomoreparties.site/login")
        email = driver.find_elements(By.XPATH, locators.TestLocators.Input_email_locator)[0]
        email.send_keys("maxx1234@yandex.ru")
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='maxx1234@yandex.ru']")))
        password = driver.find_element(By.XPATH, locators.TestLocators.Input_password_locator).send_keys("qwertyuiop")
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='qwertyuiop']")))
        driver.find_element(By.XPATH, locators.TestLocators.Log_in_locator).click()
        driver.get("https://stellarburgers.nomoreparties.site/")
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_authorization_via_recovery_form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(By.XPATH, locators.TestLocators.Recover_password_locator).click()
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        email = driver.find_element(By.XPATH, locators.TestLocators.Input_email_locator).send_keys("maxx1234@yandex.ru")
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='maxx1234@yandex.ru']")))
        driver.find_element(By.XPATH, locators.TestLocators.Recovery_button_locator).click()
        driver.get("https://stellarburgers.nomoreparties.site/reset-password")
        driver.find_element(By.XPATH, locators.TestLocators.Login_button_locator).click()
        email = driver.find_element(By.XPATH, locators.TestLocators.Input_email_locator).send_keys("maxx1234@yandex.ru")
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='maxx1234@yandex.ru']")))
        email = driver.find_element(By.XPATH, locators.TestLocators.Input_password_locator).send_keys("qwertyuiop")
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='qwertyuiop']")))
        driver.find_element(By.XPATH, locators.TestLocators.Log_in_locator).click()
        driver.get("https://stellarburgers.nomoreparties.site/register")

    def test_logout_from_account(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        personal_button = driver.find_elements(By.XPATH, locators.TestLocators.Search_personal_button_main_locator)[0]
        personal_button.click()
        driver.get("https://stellarburgers.nomoreparties.site/login")
        email = driver.find_element(By.XPATH, locators.TestLocators.Input_email_locator).send_keys("maxx1234@yandex.ru")
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='maxx1234@yandex.ru']")))
        password = driver.find_element(By.XPATH, locators.TestLocators.Input_password_locator).send_keys("qwertyuiop")
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='qwertyuiop']")))
        driver.find_element(By.XPATH, locators.TestLocators.Log_in_locator).click()
        personal_button = driver.find_element(By.XPATH,
                                              locators.TestLocators.Search_personal_button_main_locator).click()
        driver.implicitly_wait(10)
        logout_button = driver.find_element(By.XPATH, locators.TestLocators.Logout_button_locator).click()
        driver.get("https://stellarburgers.nomoreparties.site/login")
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
