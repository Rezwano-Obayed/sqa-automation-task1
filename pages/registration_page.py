from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def enter_first_name(self, first_name):
        field = self.wait.until(EC.presence_of_element_located((By.NAME, "first_name")))
        field.clear()
        field.send_keys(first_name)

    def enter_last_name(self, last_name):
        field = self.wait.until(EC.presence_of_element_located((By.NAME, "last_name")))
        field.clear()
        field.send_keys(last_name)

    def enter_email(self, email):
        field = self.wait.until(EC.presence_of_element_located((By.NAME, "email")))
        field.clear()
        field.send_keys(email)

    def enter_phone(self, phone):
        field = self.wait.until(EC.presence_of_element_located((By.NAME, "phone")))
        field.clear()
        field.send_keys(phone)

    def enter_password(self, password):
        field = self.wait.until(EC.presence_of_element_located((By.NAME, "password")))
        field.clear()
        field.send_keys(password)

    def enter_confirm_password(self, password):
        field = self.wait.until(EC.presence_of_element_located((By.NAME, "confirm_password")))
        field.clear()
        field.send_keys(password)

    def click_register(self):
        btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        btn.click()

    def get_current_url(self):
        return self.driver.current_url