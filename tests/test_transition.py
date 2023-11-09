from repos.sprint_5 import locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class TestMove:
    def test_move_to_personal_account(self, auth):
        auth.find_element(By.XPATH, locators.TestLocators.Search_personal_button_main_locator).click()
        WebDriverWait(auth, 10).until(
            expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))
        assert auth.current_url == "https://stellarburgers.nomoreparties.site/account/profile"

    def test_move_to_constructor(self, auth):
        auth.find_element(By.XPATH, locators.TestLocators.Constructor_button_locator).click()
        WebDriverWait(auth, 10).until(
            expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert auth.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_logo_moving(self, auth):
        auth.find_element(By.XPATH, locators.TestLocators.Search_personal_button_main_locator).click()
        auth.find_element(By.XPATH, locators.TestLocators.Logo_button_locator).click()
        WebDriverWait(auth, 10).until(
            expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert auth.current_url == "https://stellarburgers.nomoreparties.site/"

