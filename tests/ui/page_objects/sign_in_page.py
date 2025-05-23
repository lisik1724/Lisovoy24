from .base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = 'https://github.com/login'

    def __init__(self) ->None:
        super().__init__()
    
    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        login_elen = self.driver.find_element(By.ID, "login_field")



        login_elen.send_keys(username)


        pass_elen = self.driver.find_element(By.NAME, "password")
        

        pass_elen.send_keys(password)


        btn_elem = self.driver.find_element(By.NAME, "commit")

        
        btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title



