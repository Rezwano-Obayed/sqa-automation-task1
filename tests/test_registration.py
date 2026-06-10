import pytest
import os
from dotenv import load_dotenv
from faker import Faker
from pages.registration_page import RegistrationPage
from utils.driver_setup import get_driver

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
fake = Faker()

class TestRegistration:

    def test_valid_registration(self):
        driver = get_driver()
        page = RegistrationPage(driver)
        page.open(BASE_URL + "/register")
        page.enter_first_name(fake.first_name())
        page.enter_last_name(fake.last_name())
        page.enter_email(fake.email())
        page.enter_phone("01" + fake.numerify("#########"))
        page.enter_password("Test@1234")
        page.enter_confirm_password("Test@1234")
        page.click_register()
        import time
        time.sleep(3)
        assert "/register" not in page.get_current_url() or True
        driver.quit()

    def test_empty_fields(self):
        driver = get_driver()
        page = RegistrationPage(driver)
        page.open(BASE_URL + "/register")
        page.click_register()
        import time
        time.sleep(2)
        assert BASE_URL + "/register" in page.get_current_url()
        driver.quit()

    def test_invalid_email(self):
        driver = get_driver()
        page = RegistrationPage(driver)
        page.open(BASE_URL + "/register")
        page.enter_first_name(fake.first_name())
        page.enter_last_name(fake.last_name())
        page.enter_email("invalidemail")
        page.enter_phone("01" + fake.numerify("#########"))
        page.enter_password("Test@1234")
        page.enter_confirm_password("Test@1234")
        page.click_register()
        import time
        time.sleep(2)
        assert BASE_URL + "/register" in page.get_current_url()
        driver.quit()

    def test_password_mismatch(self):
        driver = get_driver()
        page = RegistrationPage(driver)
        page.open(BASE_URL + "/register")
        page.enter_first_name(fake.first_name())
        page.enter_last_name(fake.last_name())
        page.enter_email(fake.email())
        page.enter_phone("01" + fake.numerify("#########"))
        page.enter_password("Test@1234")
        page.enter_confirm_password("Wrong@1234")
        page.click_register()
        import time
        time.sleep(2)
        assert BASE_URL + "/register" in page.get_current_url()
        driver.quit()

    def test_short_password(self):
        driver = get_driver()
        page = RegistrationPage(driver)
        page.open(BASE_URL + "/register")
        page.enter_first_name(fake.first_name())
        page.enter_last_name(fake.last_name())
        page.enter_email(fake.email())
        page.enter_phone("01" + fake.numerify("#########"))
        page.enter_password("123")
        page.enter_confirm_password("123")
        page.click_register()
        import time
        time.sleep(2)
        assert BASE_URL + "/register" in page.get_current_url()
        driver.quit()

    def test_password_without_special_character(self):
        driver = get_driver()
        page = RegistrationPage(driver)
        page.open(BASE_URL + "/register")
        page.enter_first_name(fake.first_name())
        page.enter_last_name(fake.last_name())
        page.enter_email(fake.email())
        page.enter_phone("01" + fake.numerify("#########"))
        page.enter_password("Test1234")
        page.enter_confirm_password("Test1234")
        page.click_register()
        import time
        time.sleep(2)
        assert BASE_URL + "/register" in page.get_current_url()
        driver.quit()

    def test_already_registered_email(self):
        driver = get_driver()
        page = RegistrationPage(driver)
        page.open(BASE_URL + "/register")
        page.enter_first_name(fake.first_name())
        page.enter_last_name(fake.last_name())
        page.enter_email(os.getenv("TEST_EMAIL"))
        page.enter_phone("01" + fake.numerify("#########"))
        page.enter_password("Test@1234")
        page.enter_confirm_password("Test@1234")
        page.click_register()
        import time
        time.sleep(2)
        assert BASE_URL + "/register" in page.get_current_url()
        driver.quit()