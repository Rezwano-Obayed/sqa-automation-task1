import pytest
import os
from dotenv import load_dotenv
from pages.login_page import LoginPage
from utils.driver_setup import get_driver

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
TEST_EMAIL = os.getenv("TEST_EMAIL")
TEST_PASSWORD = os.getenv("TEST_PASSWORD")

class TestLogin:

    def test_valid_login(self):
        driver = get_driver()
        page = LoginPage(driver)
        page.open(BASE_URL + "/login")
        page.enter_email(TEST_EMAIL)
        page.enter_password(TEST_PASSWORD)
        page.click_login()
        import time
        time.sleep(3)
        assert BASE_URL + "/login" != page.get_current_url()
        driver.quit()

    def test_invalid_email(self):
        driver = get_driver()
        page = LoginPage(driver)
        page.open(BASE_URL + "/login")
        page.enter_email("wrongemail@test.com")
        page.enter_password(TEST_PASSWORD)
        page.click_login()
        import time
        time.sleep(2)
        assert page.get_error_message() != "" or BASE_URL + "/login" == page.get_current_url()
        driver.quit()

    def test_empty_fields(self):
        driver = get_driver()
        page = LoginPage(driver)
        page.open(BASE_URL + "/login")
        page.click_login()
        import time
        time.sleep(2)
        assert BASE_URL + "/login" in page.get_current_url()
        driver.quit()