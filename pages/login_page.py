from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def enter_email(self, email):
        field = self.wait.until(EC.presence_of_element_located((By.NAME, "email")))
        field.clear()
        field.send_keys(email)

    def enter_password(self, password):
        field = self.wait.until(EC.presence_of_element_located((By.NAME, "password")))
        field.clear()
        field.send_keys(password)

    def click_login(self):
        btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        btn.click()

    def get_current_url(self):
        return self.driver.current_url

    def get_error_message(self):
        try:
            error = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "text-destructive")))
            return error.text
        except:
            return ""