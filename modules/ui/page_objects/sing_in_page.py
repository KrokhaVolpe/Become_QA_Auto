from modules.ui.page_objects import BasePage
from selenium.webdriver.common.by import By


class SingInPage(BasePage):
    URL = 'https://github.com/login'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SingInPage.URL)

    def try_login(self, username, password):
        login_elem = driver.find_element(By.ID, 'login_field')
        login_elem.send_keys('username')

        pass_elem = driver.find_element(By.ID, 'password')
        pass_elem.send_keys('password')

        btn_elem = driver.find_element(By.NAME, 'commit')
        btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title