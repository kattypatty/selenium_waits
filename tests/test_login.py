from selenium.webdriver.support import expected_conditions as EC
from locators.login_locators import LoginPage_Locators
from login_page.login import LoginPage
from dotenv import load_dotenv
import os

load_dotenv()

class TestLoginPage:
    locators = LoginPage_Locators()
    wait_url = os.getenv("SELENIUM_WAITS_URL")

    # Wait for the "Begin testing" button to appear
    def test_login(self, driver):
        page = LoginPage(driver, self.wait_url)
        msg = page.login()
        assert msg == "You have successfully registered!"
        

