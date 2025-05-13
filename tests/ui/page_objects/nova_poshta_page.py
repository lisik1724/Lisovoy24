from selenium.webdriver.common.by import By
from .base_page import BasePage

class NovaPoshtaPage(BasePage):
    URL = "https://novaposhta.ua"

    def go_to(self):
        self.driver.get(self.URL)

    def track_ttn(self, number):
        input_field = self.driver.find_element(By.ID, "cargo_number")
        input_field.clear()
        input_field.send_keys(number)
        self.driver.find_element(By.ID, "cargo_search").click()

    def is_error_message_visible(self):
        self.driver.implicitly_wait(5)
        return "не знайдено" in self.driver.page_source.lower()
