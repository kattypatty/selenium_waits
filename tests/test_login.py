from selenium.webdriver.support import expected_conditions as EC
from locators.login_locators import LoginPage_Locators
from locators.src.urls import Urls
from login_page.login import LoginPage

class TestLoginPage:
    url = Urls()
    locators = LoginPage_Locators()

    # Wait for the "Begin testing" button to appear
    def test_login(self, driver):
        page = LoginPage(driver, self.url.base_url)
        msg = page.login()
        assert msg == "You have successfully registered!"
        

