import os
from dotenv import load_dotenv

from login_page.click_page import BtnPage

load_dotenv()

class TestClickBtnTest:
    btn_url = os.getenv("BUTTON_URL")

    # Testing a double click
    def test_double_click(self, driver):
        page = BtnPage(driver, self.btn_url)
        page.open()
        message_text = page.double_click_to_elem()
        assert message_text == "You have done a double click"

    # Testing a right click
    def test_right_click(self, driver):
        page = BtnPage(driver, self.btn_url)
        page.open()
        message_text = page.right_click_to_elem()
        assert message_text == "You have done a right click"

    

